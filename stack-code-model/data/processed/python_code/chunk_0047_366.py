/*
 * Copyright 2014 Mozilla Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package flash.display {
public final class GraphicsPathCommand {
  public static const NO_OP:int;
  public static const MOVE_TO:int = 1;
  public static const LINE_TO:int = 2;
  public static const CURVE_TO:int = 3;
  public static const WIDE_MOVE_TO:int = 4;
  public static const WIDE_LINE_TO:int = 5;
  public static const CUBIC_CURVE_TO:int = 6;
}
}