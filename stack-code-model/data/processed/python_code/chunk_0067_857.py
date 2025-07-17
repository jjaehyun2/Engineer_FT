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

package com.tallence.core.redirects.studio.editor.form {
import com.coremedia.ui.data.Bean;
import com.coremedia.ui.data.ValueExpression;
import com.coremedia.ui.data.ValueExpressionFactory;

import ext.container.Container;


/**
 * A form for editing redirects. Changes are bind to the localModel.
 * The localModel can be passed as a configuration parameter.
 */
public class RedirectEditPanelBase extends Container {

  public function RedirectEditPanelBase(config:RedirectEditPanel = null) {
    super(config);
  }

  protected static function getBindTo(localModel:Bean, propertyName:String):ValueExpression {
    return ValueExpressionFactory.create(propertyName, localModel);
  }

}
}