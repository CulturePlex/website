/* ----------------------------------------------------------------------------------
  $.scrolli plugin

  Encoding: UTF-8
  Version:  0.1
  Authors:
    Juan G. Hurtado   [hello@juanghurtado.com]
----------------------------------------------------------------------------------
  Table of contents
----------------------------------------------------------------------------------
  1.DEFAULT CONFIG
  2.LOCAL VARS
  3.INIT METHOD
  4.PUBLIC METHODS
    4.1.move_to_next()
    4.2.move_to_prev()
    4.3.move_to($target)
  5.PRIVATE METHODS
    5.1.update_visual_state()
    5.2.clear_timer()
  6.INITIALIZATION
  7.PLUGIN BINDING
---------------------------------------------------------------------------------- */
(function($) {
  $.scrolli = function(element, options) {

    /* =DEFAULT CONFIG
    ------------------------------------------------------------------------------ */
    var defaults = {
      showArrowPager    : true,
      showNumericPager  : true,
      pagerLeftLabel    : 'Move left',
      pagerRightLabel   : 'Move right',
      autoplay          : false,
      autoplayDelay     : 10000,
      moveSpeed         : 200,
      moveEasing        : 'linear',
      beforeMove        : function($target) {},
      afterMove         : function($target) {}
    }

    /* =LOCAL VARS
    ------------------------------------------------------------------------------ */
    var plugin    = this,
        element   = element,
        timer     = null,
        $element  = $(element),
        $scrolli  = $element,
        $wrapper,
        $elements,
        $elementWrappers,
        $currentElement,
        $pagerLeft,
        $pagerRight,
        $numericPager,
        $numericPagerItem;

    plugin.settings = {};

    /* =INIT METHOD
    ------------------------------------------------------------------------------ */
    plugin.init = function() {
      ps = plugin.settings = $.extend({}, defaults, options);

      if ($scrolli.hasClass('scrolli-processed')) {
        return;
      }

      // 1.- Build HTML wrappers
      $scrolli
        .wrap('<div class="scrolli-wrapper"></div>')
        .wrap('<div class="scrolli-overflow"></div>')
        .find('.scrolli-element')
        .wrap('<div class="scrolli-element-wrapper"></div>');

      // 2.- Define available global vars
      $wrapper          = $scrolli.parent().parent();
      $overflow         = $scrolli.parent();
      $elements         = $scrolli.find('.scrolli-element');
      $elementWrappers  = $scrolli.find('.scrolli-element-wrapper');
      $currentElement   = $elementWrappers.first();

      // 3.- Set scroller styling
      $scrolli.css({
        left : '0',
        position : 'relative',
        width : '9999em'
      });

      $overflow.css({
        overflow : 'hidden',
        position : 'relative'
      });

      $elementWrappers.css({
        'float' : 'left',
        width : $wrapper.width()
      });

      // 4.- Build arrow pager system
      if (ps.showArrowPager && $elements.length > 1) {
        $pagerLeft  = $('<a href="#" class="scrolli-pager-right">'+ ps.pagerRightLabel +'</a>');
        $pagerRight = $('<a href="#" class="scrolli-pager-left">'+ ps.pagerLeftLabel +'</a>');

        $pagerLeft.bind('click', function(e) {
          clear_timer();
          plugin.move_to_next();
          e.preventDefault();
        }).appendTo($wrapper);

        $pagerRight.bind('click', function(e) {
          clear_timer();
          plugin.move_to_prev();
          e.preventDefault();
        }).appendTo($wrapper);
      }

      // 5.- Build numeric pager system
      if (ps.showNumericPager && $elements.length > 1) {
        $numericPager     = $('<ul class="scrolli-pager"></ul>');
        $numericPagerItem = $('<li class="scrolli-pager-item"><a class="scrolli-pager-link" href="#"></a></li>');

        $elements.each(function(index) {
          $numericPagerItem.find('a').text(index + 1);
          $numericPager.append($numericPagerItem.clone());
        });

        $numericPager.find('a').bind('click', function(e) {
          plugin.move_to($elementWrappers.eq($(this).parent().index()));
          e.preventDefault();
        });

        $numericPager.appendTo($wrapper);
      }

      // 6.- Launch autoplay if needed
      if (ps.autoplay) {
        timer = setInterval(function() {
          if ($currentElement.next().length > 0) {
            plugin.move_to_next();
          } else {
            plugin.move_to($elementWrappers.first());
          }
        }, ps.autoplayDelay);
      }

      // 7.- Update visual state
      update_visual_state();

      // 8.- Mark as processed if everything was fine
      $scrolli.addClass('scrolli-processed');
    }

    /* =PUBLIC METHODS
    ------------------------------------------------------------------------------ */

    /* =|move_to_next()
     *
     *   Moves the scroller to the next element on the list
    ------------------------------------------------------------------------------ */
    plugin.move_to_next = function() {
      var $prev = $currentElement.next();
      if ($prev.length > 0) {
        plugin.move_to($prev);
      }
    }

    /* =|move_to_prev()
     *
     *   Moves the scroller to the previous element on the list
    ------------------------------------------------------------------------------ */
    plugin.move_to_prev = function() {
      var $next = $currentElement.prev();
      if ($next.length > 0) {
        plugin.move_to($next);
      }
    }

    /* =|move_to($target)
     *  - $target ($ object): Item to show
     *
     *   Moves the scroller to the target element
    ------------------------------------------------------------------------------ */
    plugin.move_to = function($target) {
      // Cancel if being moved already
      if ($scrolli.is(':animated') || $target == null || $target.length <= 0) {
        return;
      }

      // Before move callback
      ps.beforeMove($target);

      // Movement amount math
      var target_left   = ($target.index() - $currentElement.index()) * $currentElement.width(),
          current_left  = $scrolli.position().left;

      // Animation
      $scrolli.animate({
        left : (current_left - target_left) + 'px'
      },ps.moveSpeed,
        ps.moveEasing,
        ps.afterMove($target));

      $currentElement = $target;

      update_visual_state();
    }

    /* =PRIVATE METHODS
    ------------------------------------------------------------------------------ */

    /* =|update_visual_state()
     *
     *   Updates global visual state
    ------------------------------------------------------------------------------ */
    var update_visual_state = function() {
      // Arrow pager visual state
      if (ps.showArrowPager && $elements.length > 1) {
        if ($currentElement.next().length <= 0) {
          $pagerLeft.hide();
        } else {
          $pagerLeft.show();
        }

        if ($currentElement.prev().length <= 0) {
          $pagerRight.hide();
        } else {
          $pagerRight.show();
        }
      }

      // Numeric pager visual state
      if (ps.showNumericPager && $elements.length > 1) {
        $numericPager.find('.scrolli-pager-item')
        .removeClass('current')
        .eq($currentElement.index()).addClass('current');
      }

      // Current element visual state
      $elementWrappers.removeClass('current');
      $currentElement.addClass('current');
    }

    /* =|clear_timer()
     *
     *   Clears autoplay timer if exists
    ------------------------------------------------------------------------------ */
    var clear_timer = function() {
      if (ps.autoplay) {
        if (timer != null) {
          clearInterval(timer);
        }
      }
    }

    /* =INITIALIZATION
    ------------------------------------------------------------------------------ */
    plugin.init();
  }

  /* =PLUGIN BINDING
    ------------------------------------------------------------------------------ */
  $.fn.scrolli = function(options) {
    return this.each(function() {
      if (undefined == $(this).data('scrolli')) {
        var plugin = new $.scrolli(this, options);
        $(this).data('scrolli', plugin);
      }
    });
  }
})($);