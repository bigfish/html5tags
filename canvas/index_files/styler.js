function setStyleLink(link, style) {
  document.getElementById(link).disabled = link != style;
  if (link == style)
    document.getElementById(link + '-radio').checked = true;
}

function setStyle(style) {
  var date = new Date();
  date.setFullYear(date.getFullYear() + 1);
  document.cookie = 'style=' + encodeURIComponent(style) + '; expires=' + date.toGMTString() + '; path=/';
  setStyleLink('complete', style);
  setStyleLink('author', style);
  setStyleLink('highlight', style);
}

function initStyler() {
  var configUI = document.getElementById('configUI');
  var stylesUI = document.createElement('p');
  stylesUI.innerHTML =
    '<label><input type=radio name=styles id=complete-radio value=complete onchange=setStyle(value)> Normal view</label>' + 
    '<label><input type=radio name=styles id=author-radio value=author onchange=setStyle(value)> Hide UA text</label>' +
    '<label><input type=radio name=styles id=highlight-radio value=highlight onchange=setStyle(value)> Highlight UA text</label>' ;
  configUI.appendChild(stylesUI);
  // reset the style for webkit... XXX
  setStyleLink('complete', '');
  setStyleLink('author', '');
  setStyleLink('highlight', '');
  // put the style back to whatever the user last selected
  var style = getCookie('style');
  if (style != 'complete' && style != 'author' && style != 'highlight')
    style = 'complete';
  setStyle(style);
  var hashChecker = function () {
    if (style != 'author')
      return;
    var s = document.location.hash.substr(1);
    if (s.length <= 0)
      return;
    var e = document.getElementById(s);
    if (!e)
      return;
    while (e && (e != document.body)) {
      if (getComputedStyle(e, '').display == 'none') {
        var path = location.pathname;
        var file = path.substr(path.lastIndexOf('/')+1);
        showAlert('The link you followed is only available in the complete version of the specification:', file + '?style=highlight#' + s);
        return;
      }
      e = e.parentNode;
    }
  };
  window.addEventListener('hashchange', hashChecker, false);
  hashChecker();
}

var stylerTimer = new Date();
initStyler();
if (getCookie('profile') == '1')
  document.getElementsByTagName('h2')[0].textContent += '; styler.js: ' + (new Date() - stylerTimer) + 'ms';
