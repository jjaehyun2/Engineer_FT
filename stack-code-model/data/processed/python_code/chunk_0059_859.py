package com.jucasoft.flexjs.test.backbone.view {
import Backbone.View;

public class ViewA extends View {

    public function ViewA(values:*) {
        super(values);
    }

    override public function initialize(...rest):* {
        this.render();
    }

    override public function render():* {
        var template:* = _.template("<h2><%- value %></h2>");
        var aa:String = template({value: 'It - could - works!'});
        this.$el.html(aa);
        return this;
    }

}
}