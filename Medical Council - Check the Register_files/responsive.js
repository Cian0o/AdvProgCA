var winWidth;
var breakpoint = 767;
//var mobile = (/iphone|ipad|ipod|android|blackberry|mini|IEMobile|palm/i.test(navigator.userAgent.toLowerCase()));
var mobile = true;

function toggleMenu(){

    if(!$('.secondaryNav').is(':empty'))
        stepBack();

    $('#header').toggleClass('expand');
}

function toggleSearch(){

    $('#header').toggleClass('search-expand');
}

function stepBack(){
    $('.secondaryNav').empty();
    $('#header').toggleClass('x2');
     $('.primaryNav').show();
}

/*
function footerMobilise(){

    $('#footer .footer_links ul li:first-child').remove();

    $('#header #utility_link li:nth-child(3) a').text('Contact');

    var FNS00 = $('#header #utility_link li:nth-child(2)')
    var FNS01 = $('#header #utility_link li:nth-child(3)')
    var FNS02 = $('#header #utility_link li:nth-child(4)')
    var FNS03 = $('#header #utility_link li:nth-child(5)')

    $('#footer .footer_links ul').prepend($(FNS00));
    $('#footer .footer_links ul').prepend($(FNS01));
    $('#footer .footer_links ul').append($(FNS02));
    $('#footer .footer_links ul').append($(FNS03));
}
*/

function loadSecondary(obj){
    var sectionLink = obj.attr('href');
    var sectionText = obj.text();
    var sectionColor = obj.parent('li').css('background-color');

    $('.secondaryNav').load(sectionLink + " .sidebarWrapper_inner ul li", function(){
        $('.secondaryNav').prepend('<li><a href="' + sectionLink + '">Introduction</a></li>');
        $('.secondaryNav').prepend('<li class="navTitle"><h2>' + sectionText + '</h2></li>');
        $('.secondaryNav').prepend('<li class="backLnk"><a href="#" onclick="stepBack(); return false">Back</a></li>');
        $('#header').toggleClass('x2');

        $('.secondaryNav').wrap('<div class="secondaryWrap">');
        $('.secondaryWrap').css({'background-color': sectionColor});
    });
}

function checkWidth(){
    //mobile
    $('#header').prepend('<a class="menu closed" href="javascript:toggleMenu()">Menu</a>');
	$('#header').prepend('<a class="search closed" href="javascript:toggleSearch()">Search</a>');
    $('#header').append('<ul class="secondaryNav"></ul>');
    $('.search-block').append( $('#siteSearch') );

    //refactor footer for mobile
    //footerMobilise();

    $('.primaryNav a').click(function(event){
        if($(this).parent().attr('id') != 'nav_btn_006' && !$(this).parents('ul.login-buttons').length){
            loadSecondary($(this));
            event.preventDefault();
        }
    })

    if($('#homepageFlashWrapper li').length){
    	window.setTimeout(function(){
            $('.bx-window').css({'width': winWidth + 'px'});
            //get the height of the image
            var widthAspect = 950 / winWidth;
            var slideHeight = 309 / widthAspect;
            //create new height for new image text block
            slideshowHeight = slideHeight + 85;

            $('#homepageFlashWrapper').css({'height': slideshowHeight + 'px'});
            $('.bx-window').css({'height': slideshowHeight + 'px'});
            $('.bx-window ul li a').css({'height': slideshowHeight + 'px', 'width': '100%'});

            $('#homepageFlashWrapper li .banner-title-outer').attr('style','position:absolute; top:' + slideHeight + 'px');

            $('#homepageFlashWrapper li').each(function () {
                var slideTitle = $(this).find('a').attr('title')
                if (slideTitle) {
                    var splitTitle = slideTitle.split('|');
                    $(this).find('.banner-title-outer div h2').text(splitTitle[0]);
                    $(this).find('.banner-title-outer div p').text(splitTitle[1]);
                }
                $(this).find('img').css({ 'display': 'block' });
            })
    	},500)



    }
    if($('.subbanner').length){
        $('#header').prepend('<a class="home" href="/">Home</a>');
        window.setTimeout(function(){
            //get the height of the image
            var widthAspect = 950 / winWidth;
            var bannerHeight = 260 / widthAspect;

            //calculate the height to the image text
            var slideClip = ((bannerHeight / 100) * 80);
            //create new height for new image text block
            bannerHeight = slideClip + 52;

            var sectionTitle = $('.breadcrumbs li:nth-child(2)').text();
            var slideBGImg = $('.subbanner img').attr('src');

            $('.sidebar h2').text('In this section');

            $('.subbanner').css({'height': bannerHeight + 'px', 'background-image': 'url(' + slideBGImg + ')', 'background-size': 'contain' })

            var swatch = $('.mainWrapper').attr('class').split(' ')[1];
            $('.subbanner').append('<div class="banner-title-outer ' + swatch + '" style="position:absolute; bottom:0"><div><h2>' + sectionTitle + '</h2></div></div>');

        }, 500);
    }
    if($('.sidebar').length){
        if(!$('.sidebar li').length)
            $('.sidebarWrapper').remove();
        else{
            if($('li.current ul').length){
                if($('li.current ul li').length)
                    $('.sidebar li.current ul').addClass('tertiaryNav').insertBefore($('.maincontent'));
                else
                    $('.sidebar li.current ul').hide();
            }            
            if($('.sidebar').length > 1){
                $('.sidebarWrapper_inner:nth-of-type(n+2)').hide();
                $('.sidebarWrapper_inner:nth-of-type(n+2)').each(function(){
                    $('.sidebarWrapper_inner:first-child .sidebar > ul').append($(this).find('.sidebar > ul').html());
                });
            }
            $('.sidebar').addClass('collapse');

            var sectionTitle = $('.breadcrumbs li:nth-child(2)').text();

            if($('.sidebarWrapper_inner:first-child .sidebar li.current').length){
                $('.sidebarWrapper_inner:first-child .sidebar > ul').prepend('<li><a href="/' + sectionTitle.replace(/ /g,'-') + '/">Introduction</a></li>');

                var selElem = $('.sidebarWrapper_inner:first-child .sidebar li.current > a').text();
                $('.sidebarWrapper_inner:first-child .sidebar ul').prepend('<li><a href="#">' + selElem + '</a></li>');
            }
            else
                $('.sidebarWrapper_inner:first-child .sidebar > ul').prepend('<li><a href="#">Introduction</a></li>');


            $('.sidebar li:first-child').click(function(){
                $('.sidebar').toggleClass('collapse');
                event.preventDefault();
            })
        }
    }
    if($('.ResultsTable').length){
        $('.ResultsTable').replaceWith(function() {

            var $th = $(this).find('th'); // get headers
            var th = $th.map(function() {
                return $(this).text();
            }).get(); // and their values
            $th.closest('tr').remove(); // then remove them
            var $d = $('<div>', {
                'class': 'ResultsTable'
            });

            $('tr', this).each(function(i, el) {
                if($('td', this).length !=5){
                    var $div = $('<div>', {
                        'class': 'pagination'
                    }).appendTo($d);
                    $div.append($('td', this).find('table').html());
                }
                else{
                    var $div = $('<div>', {
                        'class': 'inner'
                    }).appendTo($d);
                    $('td', this).each(function(j, el) {
                        var n = j + 1;
                        var $row = $('<div>', {
                            'class': 'row'
                        });
                        $row.append(
                        $('<span>', {
                            'class': 'label',
                            text: th[j] + ':'
                        }), $('<span>', {
                            'class': 'data',
                            html: $(this).html()
                        })).appendTo($div);
                    });
                }
            });
            return $d;
        });
    }
    if($('.checkdetails').length){
        $('.checkdetails').replaceWith(function() {
            var $d = $('<div>', {
                'class': 'ResultsTable checkdetails'
            });
            $('tr', this).each(function(i, el) {
                var $div = $('<div>', {
                    'class': 'inner'
                }).appendTo($d);
                $('th', this).each(function(j, el) {
                    var n = j + 1;
                    var $row = $('<div>', {
                        'class': 'row'
                    });
                    $row.append(
                    $('<span>', {
                        'class': 'label',
                        text: $(this).html()
                    }), $('<span>', {
                        'class': 'data',
                        html: $(this).next().html()
                    })).appendTo($div);
                });
            });
            return $d;
        });
    }
    if($('object').length){
        $('object').wrap('<span class="video-container">')
    }
    if($('iframe').length){
        //$('iframe').wrap('<span class="video-container">')
    }
    if($('.maincontentWrapper .maincontent img').length){
        $('.maincontentWrapper .maincontent img').each(function(){
            if($(this).width() > (winWidth - 30))
                $(this).css({'width':'100%','height':'auto'});
        })
    }
    if($('#calendar')){
        $('#calendar').wrap('<div class="tableContainer"></div>');
        $('.tableContainer').wrap('<div class="tableContainer-outer"></div>');
        $('.tableContainer').before('<div class="tableContainer-fade"></div>');
    }
    if($('table') && $('table').width() > winWidth){
        window.setTimeout(function(){
            //console.log($('table').width());
        },200)
        /*$('table').wrap('<div class="tableContainer"></div>');
        $('.tableContainer').wrap('<div class="tableContainer-outer"></div>');
        $('.tableContainer').before('<div class="tableContainer-fade"></div>');*/
    }
    $('body').removeClass('mob');
}

function getAndroidVersion(ua) {
    var ua = ua || navigator.userAgent; 
    var match = ua.match(/Android\s([0-9\.]*)/);
    return match ? match[1] : false;
};

$(document).ready(function() {

    if(mobile && parseInt(getAndroidVersion(),10) < 3)
        mobile = false;

    winWidth = jQuery(window).width();
    var vp = document.getElementById('viewport');

    if(mobile){
        enquire.register("screen and (min-width: 768px)", {
          match : function() {
            //code here
            reView.setDefault();
          },
          deferSetup : true
        });
        enquire.register("screen and (max-width: 767px)", {
          match : function() {
            $('head').append('<link href="/includes/css/responsive.css" type="text/css" media="screen" rel="stylesheet" \/>');
            checkWidth();
          },
          deferSetup : true
        });
    }
    else{
        $('body').removeClass('mob');
    }
})

function doOrientationChange(){
    sessionStorage.removeItem("reViewMode");
    location.reload();
}

//handle orientation change for mobile
if(window.addEventListener){

  var supportsOrientationChange = "onorientationchange" in window,
      orientationEvent = "orientationchange";

  //Firefox for Android doesn't support orientationchange
  if(!supportsOrientationChange && window.matchMedia){
    var mqOrientation = window.matchMedia("(orientation: portrait)");
    mqOrientation.addListener(function() { 
        doOrientationChange();
    });
  }
  else{
    window.addEventListener(orientationEvent, function() {
        doOrientationChange();
    }, false);
  }
}