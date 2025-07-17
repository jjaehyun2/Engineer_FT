package devoron.file 
{
	import away3d.entities.Mesh;
	import away3d.library.assets.IAsset;
	import away3d.materials.TextureMaterial;
	import devoron.utils.searchandreplace.workers.SearchAndReplaceWorker.src.devoron.file.FilesObserverHelper;
	import flash.display3D.textures.TextureBase;
	/**
	 * ...
	 * @author ...
	 */
	public class FilesObserverHelper 
	{
		
		/**
		 * Перезагрузка геометрии меша.
		 * @param	geometry Новая геометрия, которую необходимо использовать.
		 * @param	mesh Старый меш, свойства которого нужно взять.
		 * @param	argsArray Ссылка на массив аргументов, относящихся к данной функции.
		 */
		private static function meshGeometryReset(geometry:IAsset, mesh:Mesh, argsArray:Array):void {
			if ( !(geometry is Geometry)) return;
			mesh.geometry = argsArray;
			// обновить аргумент для данной функции
			argsArray[0] = mesh;
		}
		
		/**
		 * Функция, позволяющая динамически обновлять текстуру у материала меша.
		 * @param	texture
		 * @param	mesh
		 * @param	argsArray
		 */
		private static function meshTextureReset(texture:IAsset, mesh:Mesh, argsArray:Array):void {
			
			if ( !(texture is TextureBase)) return;
			
			if ( (argsArray[0] as Mesh).material is TextureMaterial) {
				((argsArray[0] as Mesh).material as TextureMaterial).texture = texture as Texture2DBase;
			}
			// обновить аргумент для данной функции
			argsArray[0] = mesh;
		}
		
		private static function iconImageReset():void {
			
		}
		
		
	}

}