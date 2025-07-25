/*
 * Copyright 2019 Tallence AG
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

package com.tallence.core.redirects.studio.data {
import com.coremedia.ui.data.impl.RemoteBeanImpl;

[RestResource(uriTemplate="redirects/{siteId:[^/]+}")]
public class RedirectsImpl extends RemoteBeanImpl implements Redirects {

  public function RedirectsImpl(path:String) {
    super(path);
  }

  [ArrayElementType("com.tallence.core.redirects.studio.data.Redirect")]
  public function getItems():Array {
    return get("items");
  }

  public function getTotal():Number {
    return get("total");
  }

}

}