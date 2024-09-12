import os
import django
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path

# Configuración Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cba.settings')  # Cambia 'cba.settings' si tu configuración tiene un nombre diferente
django.setup()

from api.models import *  # Importa tus modelos

# Configuración de Google Drive
SERVICE_ACCOUNT_FILE = 'storage.json'  # Archivo de credenciales en la misma carpeta que el script
SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Carpeta en Google Drive
FOLDER_ID = '1Be3HfkroevHmPXLfpxj0nL3P6Y9oMiBk' # Reemplaza con el ID de la carpeta existente en Google Drive

def delete_files_from_folder(folder_id):
    """Elimina todos los archivos de una carpeta específica en Google Drive"""
    results = service.files().list(q=f"'{folder_id}' in parents and mimeType != 'application/vnd.google-apps.folder'", fields="files(id)").execute()
    files = results.get('files', [])
    for file in files:
        service.files().delete(fileId=file.get('id')).execute()

# Eliminar archivos de la carpeta principal (esto borrará todos los archivos en la carpeta especificada)
delete_files_from_folder(FOLDER_ID)


def create_folder(name, parent_id=None):
    """Crea una carpeta en Google Drive y devuelve su ID"""
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id] if parent_id else []
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')

def upload_file_to_drive(file_path, parent_id):
    """Sube un archivo a Google Drive en una carpeta específica y establece permisos públicos"""
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [parent_id]
    }
    media = MediaFileUpload(file_path, mimetype='image/jpeg')  # Cambia el MIME type si es necesario
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
    # Establecer permisos públicos
    permission = {
        'type': 'anyone',
        'role': 'reader'
    }
    service.permissions().create(fileId=file.get('id'), body=permission).execute()
    
    return file.get('id')


def get_or_create_folder(name, parent_id):
    """Obtiene el ID de una carpeta existente o la crea si no existe"""
    query = f"'{parent_id}' in parents and name='{name}' and mimeType='application/vnd.google-apps.folder'"
    results = service.files().list(q=query, fields="files(id)").execute()
    folders = results.get('files', [])
    if folders:
        return folders[0]['id']
    return create_folder(name, parent_id)

def upload_folder_contents(local_folder, parent_id):
    """Sube el contenido de una carpeta local a una carpeta en Google Drive"""
    for item in os.listdir(local_folder):
        local_path = os.path.join(local_folder, item)
        if os.path.isdir(local_path):
            # Crea una subcarpeta en Google Drive
            folder_id = get_or_create_folder(item, parent_id)
            # Procesa recursivamente las subcarpetas
            upload_folder_contents(local_path, folder_id)
        else:
            # Sube el archivo a Google Drive
            upload_file_to_drive(local_path, parent_id)

def update_model_images():
    media_folder = Path('media')  # Carpeta local de la que se sube contenido

    # Procesar la carpeta local y subir archivos a Google Drive
    upload_folder_contents(media_folder, FOLDER_ID)

    # Actualizar modelos con URLs de Drive
    def update_model_images_for_model(model_class, field_name):
        for obj in model_class.objects.all():
            file_path = media_folder / getattr(obj, field_name).name
            if file_path.exists():
                # Subir archivo a Google Drive y actualizar URL
                file_id = upload_file_to_drive(file_path, FOLDER_ID)
                file_url = f"https://drive.google.com/uc?export=view&id={file_id}"
                setattr(obj, field_name, file_url)
                obj.save()

    # ImagenSede
    update_model_images_for_model(ImagenSede, 'imagen')

    # UnidadProduccion
    update_model_images_for_model(UnidadProduccion, 'logo')

    # FotoUsuario
    update_model_images_for_model(FotoUsuario, 'foto')

    # Categorias
    update_model_images_for_model(Categorias, 'imagen')
    update_model_images_for_model(Categorias, 'icono')

    # Imagen
    update_model_images_for_model(Imagen, 'imagen')

    # ImagenAnuncio
    update_model_images_for_model(ImagenAnuncio, 'imagen')

    # Anuncio
    for anuncio in Anuncio.objects.all():
        # Actualizar archivo anexo
        if anuncio.anexo:
            file_path = media_folder / anuncio.anexo.name
            if file_path.exists():
                # Subir archivo a Google Drive y actualizar URL
                file_id = upload_file_to_drive(file_path, FOLDER_ID)
                file_url = f"https://drive.google.com/uc?export=view&id={file_id}"
                anuncio.anexo = file_url
                anuncio.save()

if __name__ == '__main__':
    update_model_images()
