// -*- coding: utf-8 -*-

// Copyright (c) 2009-2010 The apivk.googlecode.com project Authors.
// All rights reserved. Use of this source code is governed
// by a BSD-style license that can be found in the LICENSE file.

// url in repo: $URL$
// Author   of current version: $Author$
// Date     of current version: $Date$
// Revision of current version: $Rev$

package com.vk.api.lib
{
	import com.vk.api.APIVK;
	import flash.net.URLRequest;

	/**
	 * Описание настроек для метода <code>User.getUserSettings</code>
	 *
	 * @see User#getUserSettings()
	 */
	public class UserSett
	{

		/**
		 *  пользователь разрешил отправлять ему уведомления.
		 */
		public static const NOTIFICATION: uint = 1;

		/**
		 * доступ к друзьям
		 */
		public static const FRIENDS: uint = 2;

		/**
		 * доступ к фотографиям
		 */
		public static const PHOTOS: uint = 4;

		/**
		 * доступ к аудиозаписям
		 */
		public static const AUDIO: uint = 8;

		/**
		 * доступ к предложениям
		 */
		public static const OFFERS: uint = 32;

		/**
		 * доступ к вопросам
		 */
		public static const QUESTIONS: uint = 64;

		/**
		 * доступ к wiki-страницам
		 */
		public static const WIKI: uint = 128;

		/**
		 * доступ к меню слева
		 */
		public static const LEFT_MENU: uint = 256;

		/**
		 * публикация на стенах пользователей
		 */
		public static const WALL: uint = 512;
	}
}