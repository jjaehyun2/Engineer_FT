///////////////////////////////////////////////////////////////////////////
// Copyright (c) 2010-2011 Esri. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
///////////////////////////////////////////////////////////////////////////
package widgets.Bookmark
{

import flash.events.EventDispatcher;

[Bindable]
[RemoteClass(alias="widgets.Bookmark.Bookmark")]

public class Bookmark extends EventDispatcher
{
    public var name:String;

    public var icon:String;

    public var userCreated:Boolean;

    public var xmin:Number;
    public var ymin:Number;
    public var xmax:Number;
    public var ymax:Number;
}

}