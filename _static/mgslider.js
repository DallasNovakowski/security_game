/*
Copyright (C) 2022 Max R. P. Grossmann

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/



//from og
let efficacy = js_vars.efficacy * 100;      // import and transform constants
let endowment = (Math.round(js_vars.endowment * 100) / 100).toFixed(2);
let price = js_vars.price;
// let base_prob = js_vars.theft_success * 100;
// let lost_from_attacks = (Math.round(js_vars.lost_from_attacks * 100) / 100).toFixed(2);
// let failed_attack = (Math.round(js_vars.failed_attack * 100) / 100).toFixed(2)

// let slider = document.getElementById("sliders_here");

if(endowment>2){
    // document.getElementById("failed_attack").innerHTML = Math.round(failed_attack,0);
    // document.getElementById("lost_from_attacks").innerHTML = Math.round(lost_from_attacks,0);
    document.getElementById("endowment").innerHTML = Math.round(endowment,0);
    // document.getElementById("price").innerHTML = Math.round(price,0);
    // document.getElementById("base_prob").innerHTML = Math.round(base_prob,0);
} else {
    // document.getElementById("failed_attack").innerHTML = failed_attack;
    // document.getElementById("lost_from_attacks").innerHTML = lost_from_attacks;
    document.getElementById("endowment").innerHTML = endowment;
    // document.getElementById("price").innerHTML = price;
    // document.getElementById("base_prob").innerHTML = base_prob;
}



// document.getElementById("efficacy").innerHTML = efficacy;       // pass constants to html for in-text  BRINGING PRICE OBJECT BREAKS ALL HTML ITEMS - removing "= efficacy" doesn't seem to break things






var mgsliders = Array();

mgsliders.lookup = function (which) {
    for (var j = 0; j < mgsliders.length; j++) {
        if (mgsliders[j].field == which) {
            return mgsliders[j].obj;
        }
    }

    return undefined;
};

function mgslider(field, min, max, step) {
    this.field = field;
    this.min = parseFloat(min);
    this.max = parseFloat(max);
    this.step = parseFloat(step);
    this.digits = this.suggest_digits(step, 2);

    this.prefix = "mgslider_yF5sTZLy";
    this.yourvalue = "Your value";

    mgsliders.push({field: field, obj: this});
}

mgslider.prototype.similar = function (a, b, tolerance) {
    if (tolerance === undefined) {
        tolerance = Number.EPSILON;
    }

    return Math.abs(a-b) < tolerance;
};

mgslider.prototype.is_whole = function (x) {
    return this.similar(x, Math.floor(x)) && this.similar(x, Math.ceil(x));
};

mgslider.prototype.suggest_digits = function (x, default_) {
    for (var d = 0; d <= 9; d++) {
        var tmp = x*Math.pow(10, d);

        if (this.is_whole(tmp)) {
            return d;
        }
    }

    return default_;
};

mgslider.prototype.f2s = function (val, detect) {
    if (detect) {
        return val.toFixed(this.suggest_digits(val, this.digits)).replace("-", "&ndash;");
    }
    return val.toFixed(this.digits).replace("-", "&ndash;");
};

mgslider.prototype.id = function (id_) {
    if (id_ === undefined) {
        id_ = "";
    }

    return this.prefix + "_" + this.field + "_" + id_;
};

mgslider.prototype.markup = function () {
    return "\
        <table class='mgslider-wrapper' border='0'>\
            <tr>\
                <td class='mgslider-limit'>" + this.f2s(this.min, true) + "</td>\
                <td width='90%'>\
                    <div id='" + this.id("before") + "' class='mgslider-before' onclick='mgsliders.lookup(\"" + this.field + "\").reveal(event)'></div>\
                    <input type='range' id='" + this.id() + "' min='" + this.min + "' max='" + this.max + "' step='" + this.step + "' value='' class='mgslider form-range' oninput='mgsliders.lookup(\"" + this.field + "\").change()' onchange='mgsliders.lookup(\"" + this.field + "\").change()'>\
                </td>\
                <td class='mgslider-limit'>" + this.f2s(this.max, true) + "</td>\
            </tr>\
                <td><br></td>\
            <tr>\
                <td id='" + this.id("show") + "' class='mgslider-show' colspan='3'>" +
        `Purchasing` + " <b><span id='" + this.id("cur") + "' class='mgslider-value'></span></b> units of security, \
                you will have <b>$<span id='" + this.id("money_left") + "' class='mgslider-value'></span></b> remaining. <br> <br> \
                Once you are satisfied with your decision, please click the \"next\" button to move to the next page. <br> <br>\
</td>\
            </tr>\
        </table>\
        \
        <input type='hidden' id='" + this.id("input") + "' name='" + this.field + "' value='' />";  
};

// you will spend <b>$<span id='" + this.id("paid") + "' class='mgslider-value'></span></b>, \



mgslider.prototype.hide = function () {
    document.getElementById(this.id()).style.display = "none";
    document.getElementById(this.id("show")).style.visibility = "hidden";
    document.getElementById(this.id("show")).style.textAlign = "left";
    document.getElementById(this.id("before")).style.display = "block";
};

mgslider.prototype.print = function (el) {
    el.innerHTML += this.markup();
    this.hide();
};

mgslider.prototype.value = function () {
    return parseFloat(document.getElementById(this.id()).value);
};

mgslider.prototype.change = function () {
    document.getElementById(this.id("cur")).innerHTML = this.f2s(this.value(), false);
    document.getElementById(this.id("input")).value = this.value();
    // document.getElementById(this.id("protected")).innerHTML = this.f2s(this.value()* efficacy, false);
    if (
        // this.value() *
        price>.999999999) {
        // document.getElementById(this.id("paid")).innerHTML = (this.value() * price);
        document.getElementById(this.id("money_left")).innerHTML = (endowment - this.value() * price);
    } else {
        // document.getElementById(this.id("paid")).innerHTML = (this.value() * price).toFixed(2);
        document.getElementById(this.id("money_left")).innerHTML = (endowment - this.value() * price).toFixed(2);

    }

    // document.getElementById(this.id("new_prob")).innerHTML = this.f2s(base_prob - this.value()* efficacy, false);



};

mgslider.prototype.reveal = function (event) {
    var now;

    if (event !== undefined && typeof event.offsetX !== undefined) {
        var max = parseInt(getComputedStyle(document.getElementById(this.id("before"))).width.replace("px", ""));
        var cur = event.offsetX;

        now = (cur/max)*(this.max-this.min) + this.min;
    }
    else {
        now = this.min + Math.random()*(this.max - this.min);
    }

    now = Math.round(now/this.step)*this.step;

    document.getElementById(this.id()).style.display = "block";
    document.getElementById(this.id("before")).style.display = "none";
    document.getElementById(this.id("show")).style.visibility = "visible";

    document.getElementById(this.id()).value = now;
    this.change();
};
