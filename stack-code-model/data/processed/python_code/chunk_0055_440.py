// @todo model with same name
// @todo variant or without variant
package reader{

import uidocument.commons.api.document.*;

public class ModelsReader extends PropertiesReader {

    public function ModelsReader(dReader:UIDocumentReader) {
        super(dReader);
    }

    public function processModel(xml:XML):ModelUpdate {
        var model:ModelUpdate = DocumentObjectFactory.createModelUpdate(xml);
        model.addVariant(processVariant(xml));
        return model;
    }

    private function processVariant(xml:XML):Variant {
        var variant:Variant = DocumentObjectFactory.createVariant();
        variant.setData(processProperties(xml).getData());
        return variant;
    }

}
}