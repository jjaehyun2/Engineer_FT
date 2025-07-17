package com.illuzor.engine3d.notifications {
	
	/**
	 * Типы окон. В виде статических констант.
	 * 
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class WindowType {
		/** Отображение процесса загрузки модели */
		static public const LOADING_MODEL:String = "loadingModel";
		/** Отображение процесса загрузки текстуры */
		static public const LOADING_TEXTURE:String = "loadingTexture";
		/** Блокирующее окно. Например сообщение о фатальной ошибке */
		static public const INFO_BLOCKER:String = "infoBlocker";
		/** Окно с сообщением. Закрывается нажатием на кнопку "ОК" */
		static public const INFO_OK:String = "infoOk";
		/** Окно с сообщением. Закрывается нажатием на кнопку "ОК" */
		static public const INFO_BUTTONS:String = "infoButtons";
	}
}