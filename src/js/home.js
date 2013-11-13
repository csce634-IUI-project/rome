goog.require('goog.events');

goog.provide('hs.home');

hs.home = function () {
  goog.events.listen(document.getElementById('select-activity'),
      goog.events.EventType.CLICK, function() {
    hs.home.sendactivity('txtarea');
  });
};

hs.home.sendactivity = function (elId) {
  values = document.getElementById(elId).value.split(', ');
  hs.questions.getQuestions(values, 'activity');
};
