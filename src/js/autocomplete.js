goog.require('goog.ui.ac');

goog.provide('hs.autocomplete');

/**
 * Auto Complete helper function
 * 
 * Args:
 *   suggestion_list The list of suggested values.
 *   elId The id of the element where the auto complete will feature.
 */
hs.autocomplete = function(suggestion_list, elId) {
  matcher = new goog.ui.ac.ArrayMatcher(suggestion_list, true);
  renderer = new goog.ui.ac.Renderer(document.getElementById(elId + '-sb'));
  var inputHandler = new goog.ui.ac.InputHandler(null, null, true);

  var autoComplete = new goog.ui.ac.AutoComplete(matcher, renderer,
      inputHandler);

  inputHandler.attachAutoComplete(autoComplete);
  inputHandler.attachInputs(document.getElementById(elId));
};

