var userInputs = {};
var siteName = "Site";
var colour1 = "#020066";
var colour2 = "#800000";
var colour3 = "#fff";
var url = "/cookie-management/";
var container = "#main";
var bodyTag = "none";

function cookie(name, value, options) {
    if (typeof value != 'undefined') {
        options = options || {};
        if (value === null) {
            value = '';
            options.expires = -1;
        }
        var expires = '';
        if (options.expires && (typeof options.expires == 'number' || options.expires.toUTCString)) {
            var date;
            if (typeof options.expires == 'number') {
                date = new Date();
                date.setTime(date.getTime() + (options.expires * 24 * 60 * 60 * 1000));
            } else {
                date = options.expires;
            }
            expires = '; expires=' + date.toUTCString();
        }
        var path = options.path ? '; path=' + (options.path) : '';
        var domain = options.domain ? '; domain=' + (options.domain) : '';
        var secure = options.secure ? '; secure' : '';
        document.cookie = [name, '=', encodeURIComponent(value), expires, path, domain, secure].join('');
    } else {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
};
if (!Element.prototype.matches) {
    Element.prototype.matches = Element.prototype.msMatchesSelector ||
        Element.prototype.webkitMatchesSelector;
}

if (!Element.prototype.closest) {
    Element.prototype.closest = function (s) {
        var el = this;

        do {
            if (Element.prototype.matches.call(el, s)) return el;
            el = el.parentElement || el.parentNode;
        } while (el !== null && el.nodeType === 1);
        return null;
    };
}
"use strict";

function CookieCheck(userInputs) {
    if (userInputs.siteName != null) {
        siteName = userInputs.siteName;
    }
    try {
        if (userInputs.colours[0] != null) {
            colour1 = userInputs.colours[0];
        }
        if (userInputs.colours[1] != null) {
            colour2 = userInputs.colours[1];
        }
        if (userInputs.colours[2] != null) {
            colour3 = userInputs.colours[2];
        }
    } catch (e) {
        console.log(e);
    }
    if (userInputs.url != null) {
        url = userInputs.url;
    }
    if (userInputs.container != null) {
        container = userInputs.container;
    }
    if (userInputs.header != null) {
        bodyTag = userInputs.header[0];
    }
    var observer = new MutationObserver(function (mutations) {

        mutations.forEach(function (_ref) {
            var addedNodes = _ref.addedNodes;
            [].forEach.call(addedNodes, function (node) {
                if (node.nodeType === 1 && node.tagName === 'SCRIPT') {
                    [].forEach.call(addedNodes, function (node) {
                        if ((node.closest(container) != null && node.getAttribute('src') != null) || (node.closest("#ThirdParty"))) {
                            node.setAttribute("type", "javascript/blocked");
                            node.outerHTML = '<div class="video-block"><a href="' + url + '">Please accept all cookies to View this content</a></div>';
                        }
                        const beforeScriptExecuteListener = function (event) {
                            // Prevent only marked scripts from executing
                            if (node.getAttribute('type') === 'javascript/blocked')
                                event.preventDefault()
                            node.removeEventListener('beforescriptexecute', beforeScriptExecuteListener)
                        }
                        node.addEventListener('beforescriptexecute', beforeScriptExecuteListener)
                    });
                }

                if (node.tagName === 'IFRAME') {
                    [].forEach.call(addedNodes, function (node) {
                        if (node.closest(container) != null) {
                            node.outerHTML = '<div class="video-block"><a href="' + url + '">Please accept all cookies to View this content</a></div>';
                        }
                    });
                }
                if (node.tagName === 'OBJECT') {
                    [].forEach.call(addedNodes, function (node) {
                        if (node.closest(container) != null) {
                            node.outerHTML = '<div class="video-block"><a href="' + url + '">Please accept all cookies to View this content</a></div>';
                        }
                    });
                }
            });
        });
    });

    if (cookie("CookiePerformance") == "perfAgree" && cookie("CookieAdvertising") == "advertAgree") { }
    else {
        observer.observe(document.documentElement, {
            childList: true,
            subtree: true
        })
    }

    window.addEventListener('load', function () {
        observer.disconnect();
        if (document.cookie.indexOf(siteName + "_cookies") < 0 && bodyTag != "none") {
            AddHeader();
        }
        else if (document.cookie.indexOf(siteName + "_cookies") < 0 && bodyTag == "none") {
            document.getElementById("globalCookieBar").style.display = "block";
        }
        var ele = document.getElementById("ManageCookies");
        if (ele) {
            GenerateCookieManager();
        }
    });
}

function acceptCookie() {
    var path = "; path=/;";
    var date = new Date();
    date.setTime(date.getTime() + (182 * 24 * 60 * 60 * 1000));
    var expires = "; expires=" + date.toGMTString();
    document.cookie = siteName + "_cookies=true" + expires + path + "SameSite=Lax;";
    document.cookie = "CookiePerformance=perfAgree" + expires + path + "SameSite=Lax;";
    document.cookie = "CookieAdvertising=advertAgree" + expires + path + "SameSite=Lax;";
    document.location.reload(true);
}


function acceptIndividualCookie(Analytical, Advertising) {
    deleteAllCookies();
    var path = "; path=/;";
    document.cookie.split(';').forEach(function (c) {
        document.cookie = c.trim().split('=')[0] + '=;' + 'expires=Thu, 01 Jan 1970 00:00:00 UTC;';
    });
    var date = new Date();
    date.setTime(date.getTime() + (182 * 24 * 60 * 60 * 1000));
    var expires = "; expires=" + date.toGMTString();
    document.cookie = siteName + "_cookies=true" + expires + path + "SameSite=Lax;";
    if (Analytical === 'true') {
        document.cookie = "CookiePerformance=perfAgree" + expires + path + "SameSite=Lax;";
    }
    else {
        document.cookie = "CookiePerformance=perfDisagree" + expires + path + "SameSite=Lax;";
    }
    if (Advertising === 'true') {
        document.cookie = "CookieAdvertising=advertAgree" + expires + path + "SameSite=Lax;";
    }
    else {
        document.cookie = "CookieAdvertising=advertDisagree" + expires + path + "SameSite=Lax;";
    }
}

function GenerateCookieManager() {
    var Analytical = false;
    var Advert = false;
    if (cookie("CookiePerformance") == "perfAgree") {
        Analytical = true;
    }
    if (cookie("CookieAdvertising") == "advertAgree") {
        Advert = true;
    }
    var replace = document.getElementById("ManageCookies");
    replace.outerHTML = '<div class="cookie-panel"><h2>Choose which cookies to accept</h2>\
            <div class="panel">\
                <h3>Strictly Necessary</h3>\
                <p>Strictly necessary cookies make our website work. These cookies are essential for you to browse the website and use its features, such as page navigation, accessing secure areas of the site and complying with data protection and electronic privacy legislation. We can set these cookies without needing your consent as they are essential.</p>\
            </div>\
            <div class="panel">\
                <h3>Analytical Cookies</h3>\
                <p>Analytical cookies collect information about your use of our website, for example which pages people go to. They are essential in measuring what are the most frequently visited pages and to make sure that the website works as it should for users.</p>\
                <div class="radio-group">\
                    <div class="radio-container">\
                        <input id="AnalyticTrue" type="radio" name="analytics" value="true" ' + (Analytical == true ? 'checked="checked"' : '') + '>\
                        <label>Use analytical cookies</label>\
                    </div>\
                    <div class="radio-container">\
                        <input id="AnalyticFalse" type="radio" name="analytics" value="false" ' + (Analytical == false ? 'checked="checked"' : '') + '>\
                        <label>Do not use analytical cookies</label>\
                    </div>\
                </div>\
            </div>\
            <div class="panel">\
                <h3>Marketing Cookies</h3>\
                <p>We use marketing cookies that store user data and behaviour information. Collecting data helps us target our audience a lot more effectively according to variables.</p>\
                <div class="radio-group">\
                    <div class="radio-container">\
                        <input id="AdvertTrue" type="radio" name="marketing" value="true" ' + (Advert == true ? 'checked="checked"' : '') + '>\
                        <label>Use marketing cookies</label>\
                    </div>\
                    <div class="radio-container">\
                        <input id="AdvertFalse" type="radio" name="marketing" value="false" ' + (Advert == false ? 'checked="checked"' : '') + '>\
                        <label>Do not use marketing cookies</label>\
                    </div>\
                </div>\
            </div>\
            <div class="panel last">\
                <button id="Accept" type="button" class="btn btn-accept" onclick="ClickAccept()">Set cookie preferences</button>\
            </div>\
    </div >';
    AddStyle("manager");
}

function ClickAccept() {
    var Analytical = document.querySelector('input[name="analytics"]:checked').value;
    var Advertising = document.querySelector('input[name="marketing"]:checked').value;
    acceptIndividualCookie(Analytical, Advertising);
    window.history.back();
}
function AddStyle(type) {
    var styleContent = "";
    if (type == "header") {
        styleContent = '.cookie-warning .inner-container{width:100%;max-width:1170px;margin:30px auto;background-color:' + colour3 + ';display:flex;flex-wrap:wrap;}.cookie-warning .inner-container p{margin-bottom:0;font-size:18px;}.cookie-warning .inner-container .btn-accept{min-width:max-content;height:max-content;margin-left:20px;background-color:' + colour1 + ';color:' + colour3 + ';border:1px solid ' + colour1 + ';font-size:18px;transition:all .2s ease-in-out;margin-top:10px;padding:10px;cursor:pointer;}.cookie-warning .inner-container .btn-accept:hover{color:' + colour1 + ';background-color:' + colour3 + ';}.cookie-warning .inner-container .btn-area{display:flex;width:100%;justify-content:flex-end;}';
    }
    else {
        styleContent = '.cookie-panel{background-color:#eee;padding:20px;margin-bottom:50px;margin-top:50px;}.cookie-panel h2{margin-top:10px;}.cookie-panel .panel{background-color:#eee;padding-bottom:10px;}.cookie-panel .panel h3{font-size:22px;}.cookie-panel .panel .toggle-container{position:relative;display:inline-block;margin:0 10px;margin:5px 15px 0;align-items:baseline;}.cookie-panel .panel .toggle-container input{z-index:10;height:25px;border-radius:0;border:1px solid #424242;position:absolute;opacity:0;cursor:pointer;width:100%;}.cookie-panel .panel .toggle-container input:checked~.checkmark{background-color:#006857;}.cookie-panel .panel .toggle-container input:checked~.checkmark:after{left:18px;background-color:#fff;}.cookie-panel .panel .toggle-container .checkmark{position:relative;left:0;height:18px;width:36px;background-color:#b4083a;border:1px solid #233e4c;border-radius:20px;display:inline-block;}.cookie-panel .panel .toggle-container .checkmark:after{content:"";left:2px;width:14px;height:14px;position:absolute;background-color:#fff;border-radius:20px;top:1px;transition:.5s;}.cookie-panel .panel.last{border:none;box-shadow:none;margin-bottom:0;}.cookie-panel .radio-group .radio-container{font-weight:400;font-size:16px;font-size:1rem;line-height:1.5;clear:left;display:block;margin-bottom:8px;min-height:40px;padding:0 0 0 40px;position:relative;}.cookie-panel .radio-group .radio-container input{cursor:pointer;height:40px;left:0;margin:0;opacity:0;position:absolute;top:0;width:40px;z-index:1;}.cookie-panel .radio-group .radio-container input:checked+label:after{opacity:1;}.cookie-panel .radio-group .radio-container label{cursor:pointer;display:inline-block;margin-bottom:0;padding:3px 0 4px;touch-action:manipulation;font-weight:normal;}.cookie-panel .radio-group .radio-container label:before{background:#fff;border:2px solid #979797;border-radius:50%;box-sizing:border-box;content:"";height:28px;left:0;position:absolute;top:0;width:28px;}.cookie-panel .radio-group .radio-container label:after{background:#4c6272;border:10px solid #979797;border-radius:50%;content:"";height:0;left:4px;opacity:0;position:absolute;top:4px;width:0;}.cookie-panel .info-group .info-button{background-color:transparent;border:none;color:#337ab7;text-decoration:underline;padding-left:24px;margin-bottom:20px;margin-top:10px;position:relative;text-align:left;}.cookie-panel .info-group .info-button:hover{text-decoration:none;}.cookie-panel .info-group .info-button:before{bottom:0;content:"";left:0;margin:auto;position:absolute;top:0;display:block;width:0;height:0;border-style:solid;border-color:transparent;border-left-color:transparent;clip-path:polygon(0 0,100% 50%,0 100%);border-width:7px 0 7px 12.124px;border-left-color:inherit;}.cookie-panel .info-group .info-button.open:before{display:block;width:0;height:0;border-style:solid;border-color:transparent;border-top-color:transparent;clip-path:polygon(0 0,50% 100%,100% 0);border-width:12.124px 7px 0 7px;border-top-color:inherit;}.cookie-panel .info-group .info-button.open+.info-container{display:block;}.cookie-panel .info-group .info-container{display:none;border-left:4px solid #979797;margin-top:8px;padding:0;padding-left:16px;padding-left:24px;padding-bottom:10px;margin-bottom:25px;}.cookie-panel .info-group .info-container table{border-spacing:0;vertical-align:top;width:100%;table-layout:fixed;word-wrap:break-word;}.cookie-panel .info-group .info-container table th{border-bottom:solid #979797;}.cookie-panel .info-group .info-container table td{border-bottom:1px solid #979797;text-align:left;vertical-align:top;}.cookie-panel .info-group .info-container table th,.cookie-panel .info-group .info-container table td{padding:20px;padding-left:0;}.cookie-panel .btn-accept{background-color:' + colour1 + ';color:' + colour3 + ';border:1px solid ' + colour1 + ';font-size:18px;transition:all .2s ease-in-out;margin-top:20px;padding:10px;cursor:pointer;}.cookie-panel .btn-accept:hover{background-color:' + colour3 + ';color:' + colour1 + ';}.video-block{display:none;}';
    }
    var css = styleContent,
        head = document.head || document.getElementsByTagName('head')[0],
        style = document.createElement('style');

    head.appendChild(style);

    style.type = 'text/css';
    if (style.styleSheet) {
        // This is required for IE8 and below.
        style.styleSheet.cssText = css;
    } else {
        style.appendChild(document.createTextNode(css));
    }
}

function AddHeader() {
    AddStyle("header");
    var cookiesPolicy = userInputs.header[1] != null ? userInputs.header[1] : '/manage-cookies/';
    var ele = document.createElement('div');
    ele.classList.add("cookie-warning");
    ele.innerHTML = '<div class="inner-container">\
            <div class="text-area"><p>By using this website, you agree to the use of cookies in accordance with the Medical Council Cookie Policy. For more information on cookies, see our <a href="' + cookiesPolicy + '">Cookie Policy.</a></p></div>\
            <div class="btn-area"><a class="btn btn-accept" href="' + url + '">Manage Cookies</a><a id="closeCookieButton" class="btn btn-accept" onclick="acceptCookie();">Accept all cookies</a></div>\
        </div>';
    var appendTo = document.querySelectorAll(userInputs.header[0])[0];
    var theFirstChild = appendTo.firstChild;
    appendTo.insertBefore(ele, theFirstChild);
}

function deleteAllCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}