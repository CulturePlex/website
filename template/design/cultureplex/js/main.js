/* ---------------------------------------------------------------------------
  Global javascript

  Encoding: UTF-8
  Authors:
    Juan G. Hurtado   [hello@juanghurtado.com]
------------------------------------------------------------------------------
  Table of contents
------------------------------------------------------------------------------
  1.INIT
  2.DOCUMENT READY
--------------------------------------------------------------------------- */

if (typeof jQuery != "undefined") {

  /* =INIT
   *
   * This method initializes all JS stuff. Usually it will be called at
   * jQuery's "document ready" function, but it can also be called after
   * an Ajax DOM update or similar…
  ------------------------------------------------------------------------- */
  function init() {
    if (typeof jQuery.fn.scrolli != "undefined") {
      jQuery('.scrolli').scrolli({
        autoplay : true,
        autoplayDelay : 10000
      });

      jQuery('footer li.up a').bind('click', function(e) {
        $.scrollTo(0, 300);
        e.preventDefault();
      });
    }
  }

  /* =DOCUMENT READY
   *
   * When the documento is ready, call `init()` method.
  ------------------------------------------------------------------------- */
  jQuery(document).ready(function($) {
    jQuery('#wrapper').fadeOut(1);
    init();
  });

  jQuery(window).bind('load', function() {
    jQuery('#wrapper').fadeIn(200);
  });

}