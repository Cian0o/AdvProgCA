var j = jQuery.noConflict();

j(document).ready(function () {
    if ($('body').width() < 641) {
        var $tertiaryNav = $('.maincontentWrapper').find('ul.tertiaryNav');
        $('.maincontentWrapper').find('ul.tertiaryNav').remove();
        $('.sidebarWrapper .sidebarWrapper_inner').find('ul li.hasChildren a');
        $('ul li.hasChildren a').after($tertiaryNav.clone());
    }

    if ($('body').width() < 641) {
        $(document).ready(function () {
            
        });
    }

    // Remove blank p tags

    $('.no-grey-lines .top-left-text p').each(function () {
        var $this = $(this);
        if ($this.html().replace(/\s|&nbsp;/g, '').length == 0)
            $this.remove();
    });

     // Remove blank div (.top-right-buttons)

    if ($(window).width() < 768) {
        //Add your javascript for small screens here
        $('.no-grey-lines .top-right-buttons').each(function () {
            var $this = $(this);
            if ($this.html().replace(/\s|&nbsp;/g, '').length == 0)
                $this.remove();
        });
    }

    $('.cc_banner-wrapper  .cc_banner.cc_container.cc_container--open').each(function () {
        $(this).wrapInner('<div class="cookie-content"></div>');
    });

    $('#header').each(function () {
        $(this).wrapInner('<div class="header-content"></div>');
    });
    $('.mainWrapper.noSideCol.report.media-article, .mainWrapper.media-archive').each(function () {
        $(this).wrapInner('<div class="banner-after-header"></div>');
    });
   
    $(".home_panels p > img").each(function () {
        $(this).parent().addClass('p-img');
    })

    if ($('body').width() < 641) {
        var $loginButtons = $('#header #utilities').find('.tools');
        $('#header #utilities').find('.tools').remove();
        $('#header').find('ul.primaryNav li:last-of-type');
        $('ul.primaryNav li:last-of-type').after($loginButtons.clone());
    }

    $("#ContentPlaceHolder_Main_btnSearch").hover(function () {
        $(this).attr("src", function (index, attr) {
            return attr.replace("search-doctors-btn.gif", "search-doctors-btn-hover.jpg");
        });
    }, function () {
        $(this).attr("src", function (index, attr) {
            return attr.replace("search-doctors-btn-hover.jpg", "search-doctors-btn.gif");
        });
    });

	j(" .home_quicklinks img, .bx-auto a, .home-btn").hover(
		function() { j(this).fadeTo("fast", 0.5); },
		function() { j(this).fadeTo("fast", 1.0); }
		
	);				   
						   
	var el = j('input[type=text]');
	el.focus(function(e) {
		if (e.target.value == e.target.defaultValue)
			e.target.value = '';
	});
	
	el.blur(function(e) {
		if (e.target.value == '')
			e.target.value = e.target.defaultValue;
	});
			 
	 //Home page slider http://bxslider.com/
	var slider = j('#homepageFlashWrapper ul').bxSlider({
		auto: true,
		speed: 2000,
		pause: 5000,
		mode: 'fade',
		controls: false,
		autoControls: true,
        pager: true
	});
	
	j('#go-prev').click(function(){
	slider.goToPreviousSlide();
	return false;
	});
	
	j('#go-next').click(function(){
	slider.goToNextSlide();
	return false;
	});

	//FAQ interactivity
    if ($('.report dl, .no-grey-lines dl').length){

		$(this).find('dt').click(function(){
			var isSelected = $(this).hasClass('selected');
			isSelected ? $(this).removeClass('selected') : $(this).addClass('selected');
			isSelected ? $(this).next().hide() : $(this).next().show();
		})
	}		 
				
	if(j("#medCouncilVids").length)
	{
		// setup player without "internal" playlists
		j("medCouncilVids", "/includes/flash/flowplayer-3.2.7.swf", 
			{	
				clip: {
					baseUrl: 'http://www.medicalcouncil.ie/', 
					scaling: 'scale', 
					autoPlay: false, 
					autoBuffering: true
				}
			}
		// use playlist plugin. 
		).playlist(".mc_vid_playlist", 
			{
				playingClass: 'playing',
				pausedClass: 'paused',
				progressClass:'progress',
				loop:true
			}
		);
	}
	

	
	
	
	j(".banner_edit_icon, .documentComposite_edit_icon").hover(
		function() { j(this).toggleClass("hover"); },
		function() { j(this).toggleClass("hover"); }
	);	
	 
	
	j(".datepicker").datepicker({ 
		showOn: 'both', 
		dateFormat: 'dd/mm/yy',
		buttonImage: 'includes/images/maincontent/ico_datepicker.gif', 
		buttonImageOnly: true
	});

	j(".cma_events_imgs a").lightBox();

	j(".mainWrapper").height() > j(".sidebarWrapper").height() ? j(".sidebarWrapper").height(j(".mainWrapper").height()) : null;
	j(".maincontentWrapper").height() > j(".sidebarWrapper-archive").height() ? j(".sidebarWrapper-archive").height(j(".maincontentWrapper").height()) : null;
	j(".maincontent table").each(function(){
		if (j(this).width() > 650) {
			j(this).children("colgroup").remove();
			j(this).attr("width", "90%");
		} 
	});

	// =========================================== ASSIGN ZEBRA CLASSES TO EVERY SECOND ITEM 
	var i = 0;
	jQuery(".formRowWrapper, .maincontent .checkdetails tr").each( function(i){
		i % 2 == 0 ? jQuery(this).addClass("zebra_row_0") : jQuery(this).addClass("zebra_row_1");
		i++;
	});

	var so = new SWFObject("includes/flash/flash_1_002.swf", "flash_area", "950", "310", "8", "#ffffff");
	so.addParam("wmode", "transparent");
	if(document.getElementById("homepageFlash")) { so.write("homepageFlash"); }

	/* ------------------------------------------------ FONT SIZE TOGGLE ------------------------------------------------ */
	// If there's a cookie present for this site, assign the font size based on this value.
	if(j.cookie('fontSizeCookie'))
	{
		var getCookie = parseFloat(j.cookie('fontSizeCookie'));
		jQuery(".maincontentWrapper").css({ 'font-size' : getCookie+'em' });
	}
	
	// Increase the font size based on <current cookie size> + 0.25.
	jQuery("a.font_inc").click(function() 
	{
		if(j.cookie('fontSizeCookie'))
		{
			
			j.cookie('fontSizeCookie', parseFloat(j.cookie('fontSizeCookie'))+0.25, { path: '/' });
			jQuery(".maincontentWrapper").css({ 'font-size' : parseFloat(j.cookie('fontSizeCookie'))+'em' });
		}
		else // No Cookie Present? Set a Cookie based on initial step-up (0.25), then increase font size
		{
			j.cookie('fontSizeCookie', 1.25, { path: '/' });
			jQuery(".maincontentWrapper").css({ 'font-size' : parseFloat(j.cookie('fontSizeCookie'))+'em' });
		}
	});
	
	// Decrease the font size based on <current cookie size> - 0.25.
	jQuery("a.font_dec").click(function() 
	{
		if(j.cookie('fontSizeCookie'))
		{
			if(parseFloat(j.cookie('fontSizeCookie')) > 1.0)
			{
				j.cookie('fontSizeCookie', parseFloat(j.cookie('fontSizeCookie'))-0.25, { path: '/' });
				jQuery(".maincontentWrapper").css({ 'font-size' : parseFloat(j.cookie('fontSizeCookie'))+'em' });
			}
		}
	});
	
	/* ------------------------------------------------ FONT SIZE TOGGLE ------------------------------------------------ */

	/* ------------------------------------------------ FANCYBOX ------------------------------------------------ */

	$('a.video').click(function(e){ 
		e.preventDefault(); 
		$('.fancybox-media')
			.attr('rel', 'media-gallery')
			.fancybox({
				openEffect : 'none',
				closeEffect : 'none',
				prevEffect : 'none',
				nextEffect : 'none',

				arrows : false,
				helpers : {
					media : {},
					buttons : {}
			}
		});
	});

});