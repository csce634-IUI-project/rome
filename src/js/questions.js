goog.provide('hs.questions');

hs.questions.getQuestions = function (val, val_type) {
  values = document.getElementById('dummy-values');
  values.value = val;
  activity = document.getElementById('dummy-activity-type');
  activity.value = val_type;
  form = document.getElementById('dummy-form');
  form.action = 'questions';
  form.submit();
};