<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                      "http://www.w3.org/TR/html4/loose.dtd">
<html>
  <head>
    <title>Bug 7059 &ndash; Forking XPath</title>


<link rel="Top" href="http://www.w3.org/Bugs/Public/">

  

  


  
    <link rel="Show" title="Dependency Tree"
          href="showdependencytree.cgi?id=7059&amp;hide_resolved=1">
      <link rel="Show" title="Dependency Graph"
            href="showdependencygraph.cgi?id=7059">


      <link rel="Show" title="Bug Activity"
            href="show_activity.cgi?id=7059">
      <link rel="Show" title="Printer-Friendly Version"
            href="show_bug.cgi?format=multiple&amp;id=7059">


    

    
      <link href="skins/standard/global.css"
            rel="stylesheet"
            type="text/css">
      <link href="skins/standard/yui/calendar.css"
            rel="stylesheet"
            type="text/css">
      <link href="skins/standard/show_bug.css"
            rel="stylesheet"
            type="text/css">
    <!--[if lte IE 7]>
      
      <link href="skins/standard/IE-fixes.css"
            rel="stylesheet"
            type="text/css">
    <![endif]-->

    
        <link href="skins/standard/global.css"
              rel="stylesheet"
              title="Classic"
              type="text/css">
        <link href="skins/standard/yui/calendar.css"
              rel="stylesheet"
              title="Classic"
              type="text/css">
        <link href="skins/standard/show_bug.css"
              rel="stylesheet"
              title="Classic"
              type="text/css">
      <!--[if lte IE 7]>
      
        <link href="skins/standard/IE-fixes.css"
              rel="stylesheet"
              title="Classic"
              type="text/css">
      <![endif]-->

    
        
            <link href="skins/contrib/Dusk/global.css"
                  rel="alternate stylesheet"
                  title="Dusk"
                  type="text/css">
            <link href="skins/contrib/Dusk/yui/calendar.css"
                  rel="alternate stylesheet"
                  title="Dusk"
                  type="text/css">
            <link href="skins/contrib/Dusk/show_bug.css"
                  rel="alternate stylesheet"
                  title="Dusk"
                  type="text/css">
        <!--[if lte IE 7]>
          
          <link href="skins/contrib/Dusk/IE-fixes.css"
                rel="alternate stylesheet"
                title="Dusk"
                type="text/css">
        <![endif]-->

    

    
        <link href="skins/custom/global.css" rel="stylesheet" type="text/css">
        <link href="skins/custom/yui/calendar.css" rel="stylesheet" type="text/css">
        <link href="skins/custom/show_bug.css" rel="stylesheet" type="text/css">
    <!--[if lte IE 7]>
      
      <link href="skins/custom/IE-fixes.css"
            rel="stylesheet"
            type="text/css">
    <![endif]-->



        <script src="js/util.js" type="text/javascript"></script>
        <script src="js/field.js" type="text/javascript"></script>
        <script src="js/yui/yahoo-dom-event.js" type="text/javascript"></script>
        <script src="js/yui/calendar.js" type="text/javascript"></script>
        <script type="text/javascript">
          YAHOO.namespace('bugzilla');
          if( YAHOO.env.ua.gecko )
            YAHOO.util.Event._simpleRemove(window, "unload", YAHOO.util.Event._unload);
        </script>

    

    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla" href="./search_plugin.cgi">
    <link rel="shortcut icon" href="images/favicon.ico" >
  </head>



  <body onload=""
        class="www-w3-org-Bugs-Public bz_bug bz_status_CLOSED bz_component_HTML5_spec_&#X28;editor&#X3A;_Ian_Hickson&#X29; bz_bug_7059">




<div id="header">
<div id="banner">
        <p style="border-bottom: thin solid #dfebf7; margin-bottom: 1em;"><img src="http://www.w3.org/Icons/WWW/w3c_home_nb" alt="W3C" height="48" width="72" style="vertical-align: middle" />
	<span style="font-size: 1.4em; font-weight: bolder; color: #06358D;">Bug / Issue Tracking Service</span>
        <!-- <span>v.</span> -->
    </p>
    </div>

<table border="0" cellspacing="0" cellpadding="0" id="titles">
<tr>
    <td id="title">
      <p>Bugzilla &ndash; Bug&nbsp;7059</p>
    </td>

    <td id="subtitle">
      <p class="subheader">Forking XPath</p>
    </td>

    <td id="information">
      <p class="header_addl_info">Last modified: 2010-05-06 08:42:53</p>
    </td>
</tr>
</table>
<ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_top" name="quicksearch">
    <input class="btn" type="submit" value="Find" id="find_top"></form></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li></li>


      <li><span class="separator">| </span><a href="createaccount.cgi">New&nbsp;Account</a></li>
<li>
        <span class="separator">| </span>
        <a href="docs/html/bug_page.html" target="_blank">Help</a>
      </li>

      



      

        
      <li><span class="separator">| </span><a href="http://www.w3.org/Bugs/Public/show_bug.cgi?id=7059&amp;GoAheadAndLogIn=1">Log&nbsp;In</a></li>
</ul>

</div>

<div id="bugzilla-body">

<div class="navigation">
  
  
  <i><font color="#777777">First</font></i>
  <i><font color="#777777">Last</font></i>
  <i><font color="#777777">Prev</font></i>
  <i><font color="#777777">Next</font></i>
  &nbsp;&nbsp;
  <i><font color="#777777">No search results available</font></i>
</div>
<script type="text/javascript">
  <!--
  
  /* Outputs a link to call replyToComment(); used to reduce HTML output */
  function addReplyLink(id, real_id) {
      /* XXX this should really be updated to use the DOM Core's
       * createElement, but finding a container isn't trivial.
       */
        document.write('[<a href="#add_comment" onclick="replyToComment(' + 
                       id + ',' + real_id + ');">reply<' + '/a>]');
  }

  /* Adds the reply text to the `comment' textarea */
  function replyToComment(id, real_id) {
      var prefix = "(In reply to comment #" + id + ")\n";
      var replytext = "";
        /* pre id="comment_name_N" */
        var text_elem = document.getElementById('comment_text_'+id);
        var text = getText(text_elem);

        /* make sure we split on all newlines -- IE or Moz use \r and \n
         * respectively.
         */
        text = text.split(/\r|\n/);

        for (var i=0; i < text.length; i++) {
            replytext += "> " + text[i] + "\n"; 
        }

        replytext = prefix + replytext + "\n";


      /* <textarea id="comment"> */
      var textarea = document.getElementById('comment');
      textarea.value += replytext;

      textarea.focus();
  }

  if (typeof Node == 'undefined') {
      /* MSIE doesn't define Node, so provide a compatibility object */
      window.Node = {
          TEXT_NODE: 3,
          ENTITY_REFERENCE_NODE: 5
      };
  }

  /* Concatenates all text from element's childNodes. This is used
   * instead of innerHTML because we want the actual text (and
   * innerText is non-standard).
   */
  function getText(element) {
      var child, text = "";
      for (var i=0; i < element.childNodes.length; i++) {
          child = element.childNodes[i];
          var type = child.nodeType;
          if (type == Node.TEXT_NODE || type == Node.ENTITY_REFERENCE_NODE) {
              text += child.nodeValue;
          } else {
              /* recurse into nodes of other types */
              text += getText(child);
          }
      }
      return text;
  }


  function updateCommentTagControl(checkbox, form) {
      if (checkbox.checked) {
          form.comment.className='bz_private';
      } else {
          form.comment.className='';
      }
  }

  //-->
  </script>

<form name="changeform" method="post" action="process_bug.cgi">

  <input type="hidden" name="delta_ts" value="2010-05-06 08:42:53">
  <input type="hidden" name="longdesclength" value="43">
  <input type="hidden" name="id" value="7059">
  <input type="hidden" name="token" value="1278958373-99d776eff854f47e1ee361876195767a">
<div class="bz_alias_short_desc_container">
    
     <a href="show_bug.cgi?id=7059">
        <b>Bug&nbsp;7059</b></a> - 
     <span id="summary_alias_container" class="bz_default_hidden"> 
      <span id="short_desc_nonedit_display">Forking XPath</span>
     </span>
  
       
    <div id="summary_alias_input">
      <table id="summary">  
        
        <tr>
          <td>
            <label accesskey="s" for="short_desc"><u>S</u>ummary</label>:
          </td>
          <td>Forking XPath
          </td>
        </tr>
      </table>
    </div>
  </div>
  <script type="text/javascript">
    hideAliasAndSummary('Forking XPath', '');
  </script>
  <table>
    <tr>
      
      <td id="bz_show_bug_column_1" class="bz_show_bug_column">     
        <table>
          <tr>
    <td class="field_label">
      <b><a href="page.cgi?id=fields.html#status">Status</a></b>:
    </td>
    <td id="bz_field_status">
      <span id="static_bug_status">CLOSED
          FIXED
      </span>
    </td>
  </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          <tr>
      <td class="field_label">
        <label for="product" accesskey="p"><b><u>P</u>roduct</b></label>:
      </td><td>HTML WG
  </td>
    </tr>
        
    
    
    <tr>
      <td class="field_label">
        <label for="component" accesskey="m">
          <b><a href="describecomponents.cgi?product=HTML%20WG">
            Co<u>m</u>ponent</a>:
          </b>
        </label>
      </td><td>HTML5 spec (editor: Ian Hickson)
  </td>
    </tr>
    <tr>
      <td class="field_label">
        <label for="version"><b>Version</b></label>:
      </td>
<td>unspecified
  </td>
    </tr>
        
    
        
    <tr>
      <td class="field_label">
        <label for="rep_platform" accesskey="h"><b>Platform</b></label>:
      </td>
      <td>All
       All
       <script type="text/javascript">
         assignToDefaultOnChange(['product', 'component']);
       </script>
      </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          
          <tr>
      <td class="field_label">
        <label for="priority" accesskey="i">
          <b><a href="page.cgi?id=fields.html#importance"><u>I</u>mportance</a></b></label>:
      </td>
      <td>P2 normal
      </td>
    </tr>

      <tr>
        <td class="field_label">
          <label for="target_milestone"><b>
              <a href="http://www.w3.org/html/wg/#sched">
            Target&nbsp;Milestone</a></b></label>:
        </td><td>---
  </td>
      </tr>            
          
          <tr>
      <td class="field_label">
        <b><a href="page.cgi?id=fields.html#assigned_to">Assigned To</a></b>:
      </td>
      <td><span class="vcard"><a class="email" href="mailto:ian&#64;hixie.ch" title="ian&#64;hixie.ch" ><span class="fn">Ian 'Hixie' Hickson</span ></a></span>
      </td>
    </tr>

    <tr>
      <td class="field_label">
        <label for="qa_contact" accesskey="q"><b><u>Q</u>A Contact</b></label>:
      </td>
      <td>
<span class="vcard"><a class="email" href="mailto:public-html-bugzilla&#64;w3.org" title="public-html-bugzilla&#64;w3.org" ><span class="fn">HTML WG Bugzilla archive list</span ></a></span>
      </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          <tr>
    <td class="field_label">
      <label for="bug_file_loc" accesskey="u"><b>
          <u>U</u>RL</b></label>:
    </td>
    <td>
      <span id="bz_url_input_area">
          <a href=""></a>
      </span>
    </td>
  </tr>
  
    <tr>
      <td class="field_label">
        <label for="status_whiteboard" accesskey="w"><b><u>W</u>hiteboard</b></label>:
      </td><td colspan="2">  
  </td>
    </tr>
  
    <tr>
      <td class="field_label">
        <label for="keywords" accesskey="k">
          <b><a href="describekeywords.cgi"><u>K</u>eywords</a></b></label>:
      </td><td colspan="2">NE  
  </td>
    </tr>
          <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
          
          <tr><th class="field_label">
    <label for="dependson">Depends&nbsp;on</label>:
  </th>
  <td>    
    <span id="dependson_input_area">
    </span>
    
  </td>
  </tr>
  
  <tr><th class="field_label">
    <label for="blocked" accesskey="b"><u>B</u>locks</label>:
  </th>
  <td>    
    <span id="blocked_input_area">
    </span>
    
  </td>
  
  <tr>
    <th>&nbsp;</th>
  
    <td colspan="2" align="left" id="show_dependency_tree_or_graph">
      Show dependency <a href="showdependencytree.cgi?id=7059&amp;hide_resolved=1">tree</a>
  
        /&nbsp;<a href="showdependencygraph.cgi?id=7059">graph</a>
    </td>
  </tr>
          
        </table>
      </td>
      <td>
        <div class="bz_column_spacer">&nbsp;</div>
      </td>
      
      <td id="bz_show_bug_column_2" class="bz_show_bug_column">
        <table cellpadding="3" cellspacing="1">
        <tr>
    <td class="field_label">
      <b>Reported</b>:
    </td>
    <td>2009-06-26 14:45 by <span class="vcard"><a class="email" href="mailto:jonathan.robie&#64;redhat.com" title="jonathan.robie&#64;redhat.com" ><span class="fn">Jonathan Robie</span ></a></span>
    </td>
  </tr>
  
  <tr>
    <td class="field_label">
      <b> Modified</b>:
    </td>
    <td>2010-05-06 08:42 
      (<a href="show_activity.cgi?id=7059">History</a>)
    </td>
  
  </tr>
         
         <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr> 
         
         <tr>
    <td colspan="2" class="bz_section_spacer"></td>
  </tr>
         
                

        </table>
      </td>
    </tr>
    <tr>
      <td colspan="3">
          <hr id="bz_top_half_spacer">
      </td>
    </tr>
  </table>

  
  


<script type="text/javascript">
  <!--
  function toggle_display(link) {
    var table = document.getElementById("attachment_table");
    var rows = table.getElementsByTagName("tr");
    var originalHeight = table.offsetHeight; // Store current height for scrolling

    var toggle;
    if (link.innerHTML == "Show Obsolete") {
      toggle = ""; // This should be 'table-row', but IE 6 doesn't understand it.
      link.innerHTML = "Hide Obsolete";
    }
    else {
      toggle = "none";
      link.innerHTML = "Show Obsolete";
    }

    for (var i = 0; i < rows.length; i++) {
      if (rows[i].className.match('bz_tr_obsolete'))
        rows[i].style.display = toggle;
    }

    var newHeight = table.offsetHeight;
    window.scrollBy(0, newHeight - originalHeight);

    return false;
  }
  //-->
</script>

<br>
<table id="attachment_table" cellspacing="0" cellpadding="4">
  <tr>
    <th colspan="2" align="left">
      <a name="a0" id="a0">Attachments</a>
    </th>
  </tr>



  <tr class="bz_attach_footer">
    <td colspan="2">
      <a href="attachment.cgi?bugid=7059&amp;action=enter">Add an attachment</a>
      (proposed patch, testcase, etc.)
    </td>
  </tr>
</table>
<br>




  <br>
  <table cellpadding="1" cellspacing="1">
    <tr>
      <td id="comment_status_commit">
        <!-- The table keeps the commit button aligned with the box. -->
        <a name="add_comment"></a>
          <fieldset>
            <legend>Note</legend>
            <p>
              You need to
              <a href="show_bug.cgi?id=7059&amp;GoAheadAndLogIn=1">log in</a>
              before you can comment on or make changes to this bug.
            </p>
          </fieldset>
        
        <hr>
        <div id="comments"><script type="text/javascript">
  <!--
  function updateCommentPrivacy(checkbox, id) {
    var comment_elem = document.getElementById('comment_text_'+id).parentNode;
    if (checkbox.checked) {
      if (!comment_elem.className.match('bz_private')) {
        comment_elem.className = comment_elem.className.concat(' bz_private');
      }
    }
    else {
      comment_elem.className =
        comment_elem.className.replace(/(\s*|^)bz_private(\s*|$)/, '$2');
    }
  }

  /* The functions below expand and collapse comments  */

  function toggle_comment_display(link, comment_id) {
    var comment = document.getElementById('comment_text_' + comment_id);
    var re = new RegExp(/\bcollapsed\b/);
    if (comment.className.match(re))
        expand_comment(link, comment);
    else
        collapse_comment(link, comment);
  }

  function toggle_all_comments(action) {
    var num_comments = 43;

    // If for some given ID the comment doesn't exist, this doesn't mean
    // there are no more comments, but that the comment is private and
    // the user is not allowed to view it.

    for (var id = 0; id < num_comments; id++) {
        var comment = document.getElementById('comment_text_' + id);
        if (!comment)
            continue;

        var link = document.getElementById('comment_link_' + id);
        if (action == 'collapse')
            collapse_comment(link, comment);
        else
            expand_comment(link, comment);
    }
  }

  function collapse_comment(link, comment) {
    link.innerHTML = "(+)";
    link.title = "Expand the comment.";
    comment.className = "collapsed";
  }

  function expand_comment(link, comment) {
    link.innerHTML = "(-)";
    link.title = "Collapse the comment";
    comment.className = "";
  }

  /* This way, we are sure that browsers which do not support JS
   * won't display this link  */

  function addCollapseLink(count) {
    document.write(' <a href="#" id="comment_link_' + count +
                   '" onclick="toggle_comment_display(this, ' +  count +
                   '); return false;" title="Collapse the comment.">(-)</a> ');
  }
  //-->
  </script>








<div class="bz_comment bz_first_comment">

      <span class="bz_first_comment_head">
        
        <i>
        <a name="c0" href="show_bug.cgi?id=7059#c0">Description</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-26 14:45:44</i>

        
      </span>



<pre class="bz_comment_text" ><a href="http://www.whatwg.org/specs/web-apps/current-work/#interactions-with-xpath-and-xslt">http://www.whatwg.org/specs/web-apps/current-work/#interactions-with-xpath-and-xslt</a>
intentionally forks XPath 1.0. 

I strongly suggest that you work with XQuery and XSL Working Groups, which
produce the XPath specification, to come up with a better solution. We started
discussion on a Bugzilla bug against our spec:

<span class="bz_closed"><a href="show_bug.cgi?id=6777" title="RESOLVED INVALID - In HTML documents, no-namespace expression must match http://www.w3.org/1999/xhtml nodes">http://www.w3.org/Bugs/Public/show_bug.cgi?id=6777</a></span>

In this discussion, the reason given for forking XPath is that some people do
not want to implement XPath 2.0, which solves your problems. But instead, your
draft forks the XPath standard by creating a new version of XPath 1.0 where the
name tests have special-purpose semantics.

XPath 2.0 was published 23 January 2007 (before your Working Group was even
chartered), solves your problem, and is widely implemented. Now, in June, 2009,
you propose to create an incompatible version of XPath 1.0 and say that web
browsers must implement this instead.

And this incompatible version is not even a subset of XPath 2.0.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c1" href="show_bug.cgi?id=7059#c1">#1</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-06-26 15:18:25</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" ><span class="quote">&gt; I strongly suggest that you work with XQuery and XSL Working Groups, which</span >
produce the XPath specification, to come up with a better solution.

Note that that's what I tried first.

<span class="quote">&gt; In this discussion, the reason given for forking XPath is that some people do</span >
not want to implement XPath 2.0, which solves your problems.

Browsers have XPath 1.0 implementations and don't have XPath 2 implementations.
It isn't feasible to make the namespacing of elements in HTML DOMs gated on
browsers implementing XPath 2.0.

<span class="quote">&gt; XPath 2.0 was published 23 January 2007 (before your Working Group was even</span >
chartered), solves your problem, and is widely implemented.

What's relevant is what the status quo of XPath support in browsers is.

<span class="quote">&gt; And this incompatible version is not even a subset of XPath 2.0.</span >

I'd personally be OK with pursuing making prefixless expressions not to match
no-namespace nodes in HTML documents Gecko if the WebKit developers are OK with
making the same change to WebKit. Right now, the HTML5 spec, Gecko and WebKit
agree, so we have interop and a spec that matches implementation, which is a
pretty good situation to be in.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c2" href="show_bug.cgi?id=7059#c2">#2</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-06-26 15:27:53</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Also note that this doesn't affect XPath matching in XML documents in any way.
As far as I can tell, applying XPath to HTML documents has always been outside
the immediate interest and charter of the XSL WG.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c3" href="show_bug.cgi?id=7059#c3">#3</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-26 17:30:03</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c2">comment #2</a>)

<span class="quote">&gt; Also note that this doesn't affect XPath matching in XML documents in any way.
&gt; As far as I can tell, applying XPath to HTML documents has always been outside
&gt; the immediate interest and charter of the XSL WG.</span >

Both XQuery and XSLT are frequently applied to HTML documents. The document is
first parsed to create an XDM instance (often using tools like Tagsoup to deal
with cruft), then processed appropriately. 

Screen scraping and data integration are one important class of applications
that do this.

XPath is used in both XQuery and XSLT. It's going to be extremely confusing if
XPath expressions are interpreted differently when executed inside a browser
environment, especially since the documents that define the XPath standard do
not support this interpretation.

I suggest that you define a profile of XPath 2.0 that corresponds to the
functionality of XPath 1.0 plus default namespaces, and also define the mapping
of your XML documents to XDM (you have to do this regardless, because XPath is
defined in terms of the XDM, not the DOM). 

You may also want to allow implementations to optionally support all of XPath
2.0.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c4" href="show_bug.cgi?id=7059#c4">#4</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-26 17:37:44</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c1">comment #1</a>)
<span class="quote">&gt; &gt; I strongly suggest that you work with XQuery and XSL Working Groups, which
&gt; &gt; produce the XPath specification, to come up with a better solution.
&gt; 
&gt; Note that that's what I tried first.</span >

Let's keep working on it ... 

<span class="quote">&gt; I'd personally be OK with pursuing making prefixless expressions not to match
&gt; no-namespace nodes in HTML documents Gecko if the WebKit developers are OK with
&gt; making the same change to WebKit. Right now, the HTML5 spec, Gecko and WebKit
&gt; agree, so we have interop and a spec that matches implementation, which is a
&gt; pretty good situation to be in.</span >

But HTML documents are widely read by many applications that are not web
browsers, and some of these use XQuery or XSLT to extract data from web pages. 

XPath handling has to work in all of these environments. And the XPath language
used in all of these environments should correspond to the XPath specification.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c5" href="show_bug.cgi?id=7059#c5">#5</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-06-26 22:19:48</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Here's how I understand the situation:

* HTML5 changes HTML's processing rules such that it would break any XPath that
is currently being applied to text/html documents.
* To keep XPath 1.0 expressions working, therefore, XPath 1.0 implementations
that implement HTML5 would need to implement some changes.
* They in fact already do. For example, WebKit does what HTML5 now describes.

Personally, I would rather not have to mention XPath in the HTML5 spec; the
only reason it does mention it is to keep XPath 1.0 working.

If the XPath working group would rather this text be removed, then I would be
happy to remove it. Is that the case?</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c6" href="show_bug.cgi?id=7059#c6">#6</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-26 22:52:29</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c5">comment #5</a>)
<span class="quote">&gt; Here's how I understand the situation:
&gt; 
&gt; * HTML5 changes HTML's processing rules such that it would break any XPath that
&gt; is currently being applied to text/html documents.
&gt; * To keep XPath 1.0 expressions working, therefore, XPath 1.0 implementations
&gt; that implement HTML5 would need to implement some changes.
&gt; * They in fact already do. For example, WebKit does what HTML5 now describes.
&gt; 
&gt; Personally, I would rather not have to mention XPath in the HTML5 spec; the
&gt; only reason it does mention it is to keep XPath 1.0 working.
&gt; 
&gt; If the XPath working group would rather this text be removed, then I would be
&gt; happy to remove it. Is that the case?</span >


I'm speaking personally so far, the XQuery and XSLT Working Groups may or may
not decide to endorse any comments I make here.

If you want a language that has different semantics from XPath, I think the
clean thing to do would be to create a completely different syntax. As long as
the language is almost the same as XPath, but semantically different, I think
it is likely to be called XPath by users and to cause confusion. Some of these
same users will also be processing XML and HTML using real XPath as part of
XQuery or XSLT, but not in a web browser environment.

As far as I understand, the changes that are needed are already supported in
XPath 2.0 if you use default element namespaces and define a mapping to the
XDM, and specify that you use compatibility mode. One workable approach is to
say that you support the subset of XPath 2.0 that corresponds to the XPath 1.0
grammar.

I suspect that one or more people from our Working Group would be happy to
discuss alternatives, perhaps in a telcon or an IRC meeting.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c7" href="show_bug.cgi?id=7059#c7">#7</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-06-26 22:59:06</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >I personally have no horse in this race; I'm most happy to have HTML5 require
what the XPath working group would like it to require. Please let me know what
the XPath working group's opinion is on this topic so that I can update the
spec accordingly.

Again, the only reason we added this text in the first place was to make XPath
1.0 compatible with HTML5, which I had expected to be desired by the working
group; if such compatibility isn't desired, that's fine. (We have similar text
to make HTML5 compatible with Selectors.) I expect discussion of a new language
specifically for HTML would be best handled by a separate group; I don't think
it would belong in HTML5 proper.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c8" href="show_bug.cgi?id=7059#c8">#8</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-27 03:24:42</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Thanks - I will request that we discuss this on next Tuesday's telcon and offer
an opinion as the XML Query and XSL Working Groups. Our next meeting is June
30th.

We *definitely* want XPath to be compatible with HTML 5 documents. </pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c9" href="show_bug.cgi?id=7059#c9">#9</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:mike&#64;w3.org">Michael(tm) Smith</a>
        </span>

        2009-06-27 03:38:31</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c5">comment #5</a>)
<span class="quote">&gt; Here's how I understand the situation:
&gt; 
&gt; * HTML5 changes HTML's processing rules such that it would break any XPath that
&gt; is currently being applied to text/html documents.
&gt; * To keep XPath 1.0 expressions working, therefore, XPath 1.0 implementations
&gt; that implement HTML5 would need to implement some changes.
&gt; * They in fact already do. For example, WebKit does what HTML5 now describes.</span >

So, as a point of clarification: This seems like one of those cases where the
draft is actually descriptively documenting actual existing processing behavior
in at least one major browser, not it in fact unilaterally or arbitrarily
changing the processing rules.

<span class="quote">&gt; Personally, I would rather not have to mention XPath in the HTML5 spec; the
&gt; only reason it does mention it is to keep XPath 1.0 working.
&gt; 
&gt; If the XPath working group would rather this text be removed, then I would be
&gt; happy to remove it. Is that the case?</span >

I would be less happy for you to remove it.

I think the reason why Henri requested that it be documented is a good one, I
would like to see us try to come some agreement about how to get resolution on
this, and I think simply removing the text is not a satisfactory resolution.
The value of having the text in there now is for it to get exactly the kind of
wider review that will encourage discussion about the underlying issue that we
need to resolve here.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c10" href="show_bug.cgi?id=7059#c10">#10</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:annevk&#64;opera.com">Anne</a>
        </span>

        2009-06-27 07:02:08</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Note also that supporting XPath 2.0 or a new language does not solve the
problem. The problem is legacy XPath 1.0 expressions applying to legacy HTML
content. What changed is that legacy HTML content turns into a namespaced tree
(to make HTML and XHTML more consistent and all sorts of other smallish
benefits) and so we have to change how XPath 1.0 expressions are evaluated
because otherwise the legacy content would break.

Potential solutions:

 1. Break with XPath 1.0 as proposed.
 2. Abandon the namespaced tree approach.
 3. ???

Since 2 is an explicit design goal 1 seems like the best solution, but I'd be
interested in hearing about a potential number 3 given that a) we can keep the
tree namespaced and b) legacy XPath expressions keep working.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c11" href="show_bug.cgi?id=7059#c11">#11</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-27 23:49:30</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c10">comment #10</a>)
<span class="quote">&gt; Note also that supporting XPath 2.0 or a new language does not solve the
&gt; problem. The problem is legacy XPath 1.0 expressions applying to legacy HTML
&gt; content. What changed is that legacy HTML content turns into a namespaced tree
&gt; (to make HTML and XHTML more consistent and all sorts of other smallish
&gt; benefits) and so we have to change how XPath 1.0 expressions are evaluated
&gt; because otherwise the legacy content would break.
&gt; 
&gt; Potential solutions:
&gt; 
&gt;  1. Break with XPath 1.0 as proposed.
&gt;  2. Abandon the namespaced tree approach.
&gt;  3. ???
&gt; 
&gt; Since 2 is an explicit design goal 1 seems like the best solution, but I'd be
&gt; interested in hearing about a potential number 3 given that a) we can keep the
&gt; tree namespaced and b) legacy XPath expressions keep working.</span >

I think it would be helpful to get a small group together from your Working
Group and from the XSL and XQuery Working Groups to make sure we understand the
requirements on both sides and look for solutions.

If you are mapping both sets of HTML onto the same namespace, and you want
unprefixed names to match names in that namespace, you can do that in XPath 2.0
by declaring the default element namespace to be that namespace. An
implementation is allowed to set a default element namespace.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c12" href="show_bug.cgi?id=7059#c12">#12</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-06-28 00:04:19</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >As Anne noted, the problem is with existing deployed content using XPath 1.0,
not with future content (which as you say, is handled fine by XPath 2.0
features).</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c13" href="show_bug.cgi?id=7059#c13">#13</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-06-29 12:15:43</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c3">comment #3</a>)
<span class="quote">&gt; Both XQuery and XSLT are frequently applied to HTML documents. The document is
&gt; first parsed to create an XDM instance (often using tools like Tagsoup to deal
&gt; with cruft), then processed appropriately. </span >

But that's different. TagSoup assigns HTML elements into the
<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> namespace *like an HTML5 parser does* but legacy
browser-based HTML parsers didn't.

If you have an app that currently uses TagSoup and any version of XPath, you
don't need to change anything on the XPath layer if you move from TagSoup to an
HTML5-compliant parser.

<span class="quote">&gt; Screen scraping and data integration are one important class of applications
&gt; that do this.</span >

Indeed, but they have nothing to do with this special case in the spec.

In the screen scraping scenario, the XPath expressions are supplied by the
scraper developer--not by the remote Web content. The issue at hand has
everything to do with the case where the XPath 1.0 expressions are supplied by
existing content in JavaScript programs using the document.evaluate API.

Hixie, I think the spec should make it clearer that the willful violation of
XPath 1.0 only applies to UAs that support scripting and let scripts in content
evaluate XPath expressions against the DOM.

<span class="quote">&gt; XPath is used in both XQuery and XSLT. It's going to be extremely confusing if
&gt; XPath expressions are interpreted differently when executed inside a browser
&gt; environment, especially since the documents that define the XPath standard do
&gt; not support this interpretation.</span >

Frankly, I think most users of XPath will never even realize that this hack is
in place and, therefore, won't be confused by it.

<span class="quote">&gt; I suggest that you define a profile of XPath 2.0 that corresponds to the
&gt; functionality of XPath 1.0 plus default namespaces, and also define the mapping
&gt; of your XML documents to XDM (you have to do this regardless, because XPath is
&gt; defined in terms of the XDM, not the DOM). </span >

The point of having this in the spec is to provide advice to implementors who
have XPath 1.0 engines but haven't upgraded to DOM5 yet. When I implemented
this for Gecko, I first had to experience test case failures and then go find
out what WebKit does. The only reason I'm pursuing this is that I want to do
unto the next implementor what I wish the previous implementor had done unto
me.

(In reply to <a href="show_bug.cgi?id=7059#c6">comment #6</a>)
<span class="quote">&gt; If you want a language that has different semantics from XPath, I think the
&gt; clean thing to do would be to create a completely different syntax.</span >

That's completely infeasible, since the whole point is to keep existing XPath
1.0 expressions, which are already part of existing script out there, working.

(In reply to <a href="show_bug.cgi?id=7059#c11">comment #11</a>)
<span class="quote">&gt; (In reply to <a href="show_bug.cgi?id=7059#c10">comment #10</a>)
&gt; I think it would be helpful to get a small group together from your Working
&gt; Group and from the XSL and XQuery Working Groups to make sure we understand the
&gt; requirements on both sides and look for solutions.</span >

Here are the requirements for the case where the UA accepts XPath 1.0
expressions from Web content through scripting:

 1) Prefixless name expressions in XPath 1.0 expressions passed to
document.evaluate() must match against HTML element nodes in HTML documents
(for existing expressions). This requirement is not negotiable. It's a
non-starter to suggest that a browser vendor whose previous release exhibits
this behavior make their next release not exhibit this behavior.

 2) Name expressions whose namespace <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> should match
against HTML element nodes in HTML documents (for prospective expressions).
This isn't a hard requirement, but not having this property would hinder
expression portability between HTML and XHTML.

 3) The solution must not require browser vendors who currently ship XPath 1.0
engines to upgrade to an XPath 2.x engine. This is practically a hard
requirement.

 4) HTML element nodes in the DOM should report <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> as
their namespace. (Note that giving up on this point would require special
casing all over while putting the hack in the XPath matcher isolates the hack.
Also note that this property removes the need of a hack from Selectors. As a
consequence, it's safe to consider this as a pretty serious requirement at this
point.)

 5) It's more important for different browsers to do the same thing than for
some browsers to be more purely XPath 2.0-like.

 6) The XPath engine shouldn't have to modify its behavior depending on whether
the expression came in via document.evaluate() or other means. This is a fairly
hard requirement.

Here are the requirements for other cases (already satisfied by TagSoup +
off-the-shelf XPath library):

 A) Name expressions whose namespace <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> should also
match against HTML element nodes in HTML documents.

 B) HTML elements should be in the <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> namespace.

- -

As you can see, the only degree of freedom here for UAs that support scripting
and document.evaluate() is whether no-namespace expressions match against
no-namespace element nodes *in addition to* matching against HTML nodes. And
even in that case, uniformity between browsers is more important than being a
purer subset of XPath 2.0.

There's no impact on applications that don't get their XPath expressions from
Web content but whose XPath expressions are supplied by the application
developer.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c14" href="show_bug.cgi?id=7059#c14">#14</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-06-29 16:21:36</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >As I understand, you want a path expression with no prefixes to match elements
from either documents whose HTML elements are in no namespace, or documents
whose HTML elements are in the HTML namespace.

As I understand, this affects only document.evaluate(), which applies only to
one document at a time.

Did I get that right? If so, I'll make sure we discuss this in the Working
Groups tomorrow and make a recommendation. If I'm missing or misunderstanding
requirement, please let me know.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c15" href="show_bug.cgi?id=7059#c15">#15</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-06-30 06:31:57</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c14">comment #14</a>)
<span class="quote">&gt; As I understand, you want a path expression with no prefixes to match elements
&gt; from either documents whose HTML elements are in no namespace, or documents
&gt; whose HTML elements are in the HTML namespace.</span >

No. As of HTML5, HTML elements (elements that implement the HTMLElement DOM
interface) are always in the <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> namespace (like with
TagSoup). Elements that aren't in a namespace aren't HTML elements (and,
therefore, don't implement the HTMLElement interface). All parser-inserted
element nodes in HTML documents are in one of these three namespaces:
<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>
<a href="http://www.w3.org/2000/svg">http://www.w3.org/2000/svg</a>
<a href="http://www.w3.org/1998/Math/MathML">http://www.w3.org/1998/Math/MathML</a>

The HTMLness of a document is an implementation-internal boolean on the object
that implements the Document interface. &quot;HTML document&quot; refers to a DOM tree
with the HTMLness bit set--not to the byte stream. (&quot;Document&quot; refers to the
parsed representation--not to the source text here.)

No-namespace nodes can be introduced to HTML documents only by a script calling
createElementNS(null, ...) or by moving a no-namespace node from an XML
document into an HTML document. 

(Note that XSLT cannot introduce no-namespace nodes into HTML documents,
because the namespace is changed to <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> when an XSLT
program tries to do so: <span class="bz_closed"><a href="show_bug.cgi?id=6776" title="VERIFIED FIXED - Note the XSLT implications of assigning HTML elements into the http://www.w3.org/1999/xhtml namespace">bug 6776</a></span>. Also note that XSLT programs still can
introduce no-namespace nodes into XML documents, i.e. documents whose HTMLness
bit is false.)

For compatibility with existing XPath 1.0 expressions whose authors have
assumed that HTML elements aren't in a namespace, no-namespace XPath
expressions need to match against nodes whose namespace is
<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> when the owner document of those nodes has been
marked as an HTML document. 

<span class="quote">&gt; As I understand, this affects only document.evaluate(), which applies only to
&gt; one document at a time.</span >

This affects any API that allows the evaluation of XPath expressions against
DOM trees whose HTMLness bit is true. Thus, it also applies to the
XSLTProcessor API:
<a href="https://developer.mozilla.org/en/Using_the_Mozilla_JavaScript_interface_to_XSL_Transformations">https://developer.mozilla.org/en/Using_the_Mozilla_JavaScript_interface_to_XSL_Transformations</a>

Note that when XSLT is applied to an XML document that has the xml-stylesheet
PI and that is being loaded from the network, the input DOM doesn't have the
HTMLness bit set, so this doesn't apply.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c16" href="show_bug.cgi?id=7059#c16">#16</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-07-03 12:50:47</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >I think wording similar to this would meet your requirements, as I understand
them:

In XPath 1.0, if a NameTest has no prefix, then the namespace URI is null. In
the context of document.evaluate(), if a NameTest has no prefix, the namespace
URI is <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> if the principle node type of the NameTest
is element; otherwise, it has no namespace URI.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c17" href="show_bug.cgi?id=7059#c17">#17</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-07-07 10:37:06</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Does that formulation affect testing expressions against attribute names?</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c18" href="show_bug.cgi?id=7059#c18">#18</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-07-07 11:23:00</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c17">comment #17</a>)
<span class="quote">&gt; Does that formulation affect testing expressions against attribute names?</span >

No. That would have been clearer if I had said &quot;is null&quot; in both places,
instead of &quot;is null&quot; in one place and &quot;has no namespace URI&quot; in the other. So
this is better wording:

&quot;In XPath 1.0, if a NameTest has no prefix, then the namespace URI is null. In
the context of document.evaluate(), HTML5 specifies a different default element
namespace: if a NameTest has no prefix and the principle node type of the
NameTest is element, the namespace URI is <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>; if a
NameTest has no prefix and the principle node type of the NameTest is not
element, the namespace URI is null.&quot;</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c19" href="show_bug.cgi?id=7059#c19">#19</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jim.melton&#64;acm.org">Jim Melton</a>
        </span>

        2009-08-27 22:41:25</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >The XML Query WG plans to meet at TPAC 2009 (Technical Plenary and Advisory
Council meeting).  We think that it would be beneficial for the XML Query and
HTML WGs to get together for an hour or two during that week to discuss this
issue.  To that end, I'm sending separate email to the chair(s) of the HTML WG
containing this suggestion. 

Jim Melton, Chair of the XML Query WG</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c20" href="show_bug.cgi?id=7059#c20">#20</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-08-28 07:41:11</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >If I understand <a href="show_bug.cgi?id=7059#c18">comment 18</a> right, the only change it makes to the current HTML
5 spec is flipping the detail that I called the only degree of freedom in
<a href="show_bug.cgi?id=7059#c13">comment 13</a> the other way round. That is, compared to the current HTML 5 spec,
the difference is that a prefixless name expression wouldn't match a
no-namespace element node in a tree flagged as HTML.

I'm willing to pursue a patch with this change in Gecko if WebKit devs are also
willing to change WebKit likewise.

In any case, the spec text needs to be scoped to anything that causes XPath
expressions to be evaluated against an HTML DOM in a browser--not just
document.evaluate(). For example, this would also need to apply to invoking an
XSLT transform from JS with an HTML input document.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c21" href="show_bug.cgi?id=7059#c21">#21</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:mjs&#64;apple.com">Maciej Stachowiak</a>
        </span>

        2009-08-28 07:53:36</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c20">comment #20</a>)
<span class="quote">&gt; If I understand <a href="show_bug.cgi?id=7059#c18">comment 18</a> right, the only change it makes to the current HTML
&gt; 5 spec is flipping the detail that I called the only degree of freedom in
&gt; <a href="show_bug.cgi?id=7059#c13">comment 13</a> the other way round. That is, compared to the current HTML 5 spec,
&gt; the difference is that a prefixless name expression wouldn't match a
&gt; no-namespace element node in a tree flagged as HTML.
&gt; 
&gt; I'm willing to pursue a patch with this change in Gecko if WebKit devs are also
&gt; willing to change WebKit likewise.
&gt; </span >

I believe we'd be willing to change this in WebKit.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c22" href="show_bug.cgi?id=7059#c22">#22</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-07 10:30:20</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >I added the new condition. I hope that's what was intended. If it wasn't please
reopen the bug with the exact text changes you would like.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c23" href="show_bug.cgi?id=7059#c23">#23</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:mike&#64;w3.org">Michael(tm) Smith</a>
        </span>

        2009-09-09 03:46:42</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c22">comment #22</a>)
<span class="quote">&gt; I added the new condition. I hope that's what was intended. If it wasn't please
&gt; reopen the bug with the exact text changes you would like.</span >

for the record, the diff for the change is here:

<a href="http://html5.org/tools/web-apps-tracker?from=3764&amp;to=3765">http://html5.org/tools/web-apps-tracker?from=3764&amp;to=3765</a>

The newly added text reads:

[[
Irrespective of the requirements defined in XPath 1.0, a name expression must
not evaluate to matching a node when the following conditions are all met:

  - The name expression has no namespace.
  - The expression is being tested against an element node.
  - The element is in no namespace.
  - The element's document is an HTML document.
]]</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c24" href="show_bug.cgi?id=7059#c24">#24</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-09 11:48:15</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >The latest change, and the associated diffs, add more special purpose semantics
to the processing of HTML using XPath. That does not address the bug.

XPath defines what name expressions do. They should work the same way for HTML
as for XML.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c25" href="show_bug.cgi?id=7059#c25">#25</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-09-09 11:54:42</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c24">comment #24</a>)
<span class="quote">&gt; The latest change, and the associated diffs, add more special purpose semantics
&gt; to the processing of HTML using XPath. That does not address the bug.
&gt; 
&gt; XPath defines what name expressions do. They should work the same way for HTML
&gt; as for XML.</span >

How does the effect of the current spec text differ from the effect of what you
suggested in <a href="show_bug.cgi?id=7059#c18">comment 18</a>? If it differs in any way, my <a href="show_bug.cgi?id=7059#c20">comment 20</a> is based on a
misunderstanding.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c26" href="show_bug.cgi?id=7059#c26">#26</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-09 12:18:35</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >First off, I believe that our Working Groups have agreed to meet to discuss
this issue. I suggest that we not resolve the issue before that discussion.

The suggestion in <a href="show_bug.cgi?id=7059#c18">comment #18</a> is that you use the XPath 1.0 semantics as
defined in that specification, and be clear about the default namespace:

<span class="quote">&gt; In XPath 1.0, if a NameTest has no prefix, 
&gt; then the namespace URI is null. In the context 
&gt; of document.evaluate(), HTML5 specifies a different 
&gt; default element namespace: if a NameTest has no prefix 
&gt; and the principle node type of the NameTest is element, 
&gt; the namespace URI is <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>; if a
&gt; NameTest has no prefix and the principle node type of the 
&gt; NameTest is not element, the namespace URI is null.</span >


What I see in the current draft gives match conditions in addition to those
defined in XPath 1.0, plus match conditions defined in XPath 1.0 that do not
apply, and says that it is willfully violating the XPath specification.

<span class="quote">&gt; In addition to the cases where a name expression would match a
&gt; node per XPath 1.0, a name expression must evaluate to matching a
&gt; node when all the following conditions are also met:
&gt; 
&gt;     * The name expression has no namespace.
&gt;     * The name expression has local name that is a match for local.
&gt;     * The expression is being tested against an element node.
&gt;     * The element has local name local.
&gt;     * The element is in the HTML namespace.
&gt;     * The element's document is an HTML document.
&gt; 
&gt; Irrespective of the requirements defined in XPath 1.0, a name
&gt; expression must not evaluate to matching a node when the
&gt; following conditions are all met:
&gt; 
&gt;     * The name expression has no namespace.
&gt;     * The expression is being tested against an element node.
&gt;     * The element is in no namespace.
&gt;     * The element's document is an HTML document.
&gt; 
&gt; These requirements are a willful violation of the XPath 1.0
&gt; specification, motivated by desire to have implementations be
&gt; compatible with legacy content while still supporting the changes
&gt; that this specification introduces to HTML regarding which
&gt; namespace is used for HTML elements. [XPATH10]</span ></pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c27" href="show_bug.cgi?id=7059#c27">#27</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-09 12:59:50</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c25">comment #25</a>)

<span class="quote">&gt; How does the effect of the current spec text differ from the effect of what you
&gt; suggested in <a href="show_bug.cgi?id=7059#c18">comment 18</a>? If it differs in any way, my <a href="show_bug.cgi?id=7059#c20">comment 20</a> is based on a
&gt; misunderstanding.</span >

I believe the effect is the same - but it is very difficult for the reader to
determine whether this is true or not, because the text currently adds some
cases to what XPath 1.0 specifies, then makes some restrictions that XPath 1.0
does not contain.

Perhaps the two WGs, when we meet, could usefully discuss whether there are any
differences in the end result.

But I also think that the language of the XHTML specification should read more
like <a href="show_bug.cgi?id=7059#c18">comment #18</a> than like what it currently contains, i.e. it should conform
to what XPath 1.0 says except for the default element namespace, rather than
make two changes to how name tests work, add a note saying that it willfully
violates the XPath 1.0 specification, and hoping that the reader can realize
that if you think about it hard enough, the only real difference is the default
element namespace. </pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c28" href="show_bug.cgi?id=7059#c28">#28</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-09 23:38:12</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >We're not going to delay the spec until such time as the workings groups can
meet — the HTML working group is literally hundreds of people, so all we'd
ever be able to do is have a subset of the group meet, like we're doing at the
TPAC. Plus, such a group from the HTMLWG would by charter be unable to make any
decisions, anyway, since we have to make decisions in a way that allows
asynchronous participation.

If you don't want the spec to say what it says now, could you be more precise
about what you would like it to say, and how that differs from what it says?</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c29" href="show_bug.cgi?id=7059#c29">#29</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:hsivonen&#64;iki.fi">Henri Sivonen</a>
        </span>

        2009-09-10 07:50:23</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c28">comment #28</a>)
<span class="quote">&gt; We're not going to delay the spec until such time as the workings groups can
&gt; meet — the HTML working group is literally hundreds of people, so all we'd
&gt; ever be able to do is have a subset of the group meet, like we're doing at the
&gt; TPAC. Plus, such a group from the HTMLWG would by charter be unable to make any
&gt; decisions, anyway, since we have to make decisions in a way that allows
&gt; asynchronous participation.</span >

I won't be at TPAC.

(In reply to <a href="show_bug.cgi?id=7059#c27">comment #27</a>)
<span class="quote">&gt; (In reply to <a href="show_bug.cgi?id=7059#c25">comment #25</a>)
&gt; 
&gt; &gt; How does the effect of the current spec text differ from the effect of what you
&gt; &gt; suggested in <a href="show_bug.cgi?id=7059#c18">comment 18</a>? If it differs in any way, my <a href="show_bug.cgi?id=7059#c20">comment 20</a> is based on a
&gt; &gt; misunderstanding.
&gt; 
&gt; I believe the effect is the same </span >

Great!

<span class="quote">&gt; but it is very difficult for the reader to
&gt; determine whether this is true or not, because the text currently adds some
&gt; cases to what XPath 1.0 specifies, then makes some restrictions that XPath 1.0
&gt; does not contain.</span >

Isn't that what any delta spec does?

<span class="quote">&gt; But I also think that the language of the XHTML specification should read more
&gt; like <a href="show_bug.cgi?id=7059#c18">comment #18</a> than like what it currently contains, i.e. it should conform
&gt; to what XPath 1.0 says except for the default element namespace, rather than
&gt; make two changes to how name tests work, add a note saying that it willfully
&gt; violates the XPath 1.0 specification, and hoping that the reader can realize
&gt; that if you think about it hard enough, the only real difference is the default
&gt; element namespace.</span >

I disagree. I think the way the spec is currently worded requires the least
amount of thought on the behalf of the implementor who is hacking the delta to
an existing XPath 1.0 implementation. After all, what's in the spec in the
implementation delta that is needed (with or without the edit from rev 3765).
If even you can't immediately see if your wording matches this delta, your
wording isn't obvious enough.

Invoking the concept of &quot;default namespace&quot; doesn't make sense, because it is
an XPath 2.0 concept and HTML5 is specifying a delta on top of XPath 1.0.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c30" href="show_bug.cgi?id=7059#c30">#30</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-10 13:43:02</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c28">comment #28</a>)
<span class="quote">&gt; We're not going to delay the spec until such time as the workings groups can
&gt; meet — the HTML working group is literally hundreds of people, so all we'd
&gt; ever be able to do is have a subset of the group meet, like we're doing at the
&gt; TPAC. Plus, such a group from the HTMLWG would by charter be unable to make any
&gt; decisions, anyway, since we have to make decisions in a way that allows
&gt; asynchronous participation.</span >

Asynchronous participation is fine with me - from my email, it looks like our
chair proposed to have some members of your WG join our WGs telcon on the 15th
(Maciej Stachowiak also pointed out that this needs to be resolved before
TPAC).

Currently, the chairs of our two working groups are communicating about this,
and it's pretty clear that our WG does not consider this resolved yet. I
suggest we leave it open until we reach agreement.

<span class="quote">&gt; If you don't want the spec to say what it says now, could you be more precise
&gt; about what you would like it to say, and how that differs from what it says?</span >

Commend #18 was my attempt to do this. It is not an official response from the
XML Query WG, merely wording that I thought solved the problem.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c31" href="show_bug.cgi?id=7059#c31">#31</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-10 14:54:48</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c29">comment #29</a>)

<span class="quote">&gt; Isn't that what any delta spec does?</span >

HTML5 should not be a delta spec for XPath 1.0. If it were, that would be
forking XPath.

<span class="quote">&gt; I disagree. I think the way the spec is currently worded requires the least
&gt; amount of thought on the behalf of the implementor who is hacking the delta to
&gt; an existing XPath 1.0 implementation. After all, what's in the spec in the
&gt; implementation delta that is needed (with or without the edit from rev 3765).
&gt; If even you can't immediately see if your wording matches this delta, your
&gt; wording isn't obvious enough.
&gt; 
&gt; Invoking the concept of &quot;default namespace&quot; doesn't make sense, because it is
&gt; an XPath 2.0 concept and HTML5 is specifying a delta on top of XPath 1.0.</span >

The advantage of invoking the concept of a default element namespace is that
XPath 2.0 - which is the successor of XPath 1.0, not a private fork - already
uses this concept to provide the functionality you want to provide using a
different concept.

I think there are some issues with your current wording, and it is easier to
adopt wording like what I suggested in <a href="show_bug.cgi?id=7059#c18">comment 18</a> than to fix this - let me try
to explain.

* The name expression has no namespace.

There is no such thing as a &quot;name expression&quot;, you mean a NameTest. I think you
mean to say &quot;The NameTest has no prefix&quot;.

* The name expression has local name that is a match for local.

I think you mean to say that the local part of the NameTest matches the local
name 'local'.

* The expression is being tested against an element node.

I would describe this in terms of what the NameTest specifies - the default
element namespace is used for an unprefixed QName appearing in a position where
an element name is expected.


If I make those changes to both bullet lists in your spec, then the first
bullet list says that unprefixed NameTests for elements in an HTML document
must match elements in the HTML namespace, and the second bullet list says that
unprefixed Nametests for elements in an HTML document must not match elements
that have no namespace. 

And in that case, this is equivalent to my language in <a href="show_bug.cgi?id=7059#c18">comment #18</a>, except that
I forgot to mention this is true only for HTML documents:

&quot;In XPath 1.0, if a NameTest has no prefix, then the namespace URI is null. In
the context of document.evaluate(), HTML5 specifies a default element namespace
&lt;add&gt;for HTML documents&lt;/add&gt;: if a NameTest has no prefix and the  rinciple
node type of the NameTest is element, the namespace URI is 
<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>; if a NameTest has no prefix and the principle
node type of the NameTest is not element, the namespace URI is null.&quot;

If you want to be clear that default element namespaces were added in XPath
2.0, you could state that in a NOTE.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c32" href="show_bug.cgi?id=7059#c32">#32</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-11 00:19:36</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >&quot;NameTest&quot; appears to be nothing but a token in the XPath grammar, so I don't
understand what it means to talk about it matching elements or anything like
that. 
Also, it's hard to determine, out of context, if your proposed text is stating
a fact that can be derived from other requirements, or if it is intended to be
introducing new requirements.

How about this text:

A node test consisting of a QName with no prefix (i.e. that matches the
UnprefixedName production) must be treated as if it instead had the namespace
URI equal to HTML namespace when the node is an element whose document is an
HTML document. [XPATH10] [XMLNS]</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c33" href="show_bug.cgi?id=7059#c33">#33</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-11 13:22:04</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c32">comment #32</a>)
<span class="quote">&gt; &quot;NameTest&quot; appears to be nothing but a token in the XPath grammar, so I don't
&gt; understand what it means to talk about it matching elements or anything like
&gt; that. 
&gt; Also, it's hard to determine, out of context, if your proposed text is stating
&gt; a fact that can be derived from other requirements, or if it is intended to be
&gt; introducing new requirements.
&gt; 
&gt; How about this text:
&gt; 
&gt; A node test consisting of a QName with no prefix (i.e. that matches the
&gt; UnprefixedName production) must be treated as if it instead had the namespace
&gt; URI equal to HTML namespace when the node is an element whose document is an
&gt; HTML document. [XPATH10] [XMLNS]</span >

This is a *lot* closer. I would change &quot;must be treated as if it instead had&quot;
to &quot;has&quot;, and also make it clear that it is the path expression, and not the
document, that determines whether the node test is testing an element name.

Here's my best shot at this:

&quot;A node test consisting of a QName with no prefix (i.e. that matches the
UnprefixedName production) 
has the namespace URI <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> (the HTML namespace)
when the node test occurs in a position where an element or type name is
expected
and the path expression is applied to a document that is an HTML document.
[XPATH10] [XMLNS]&quot;

I would also change the note, since this is no longer such a willful violation:

Note: This is equivalent to adding the default element namespace feature of
XPath 2.0 to XPath 1.0, and using the HTML namespace as the default element
namespace for HTML documents. It is motivated by the desire to have
implementations be compatible with legacy HTML content while still supporting
the changes that this specification introduces to HTML regarding the namespace
used for HTML elements, and by the desire to use XPath 1.0 rather than XPath
2.0.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c34" href="show_bug.cgi?id=7059#c34">#34</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-11 22:51:43</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" ><span class="quote">&gt; This is a *lot* closer. I would change &quot;must be treated as if it instead had&quot;
&gt; to &quot;has&quot;</span >

It has to say &quot;must&quot; otherwise there's no normative conformance criteria, and
it becomes impossible to determine if it's a statement trying to modify XPath,
or a statement trying to describe the results of other conformance criteria
(and failing).


<span class="quote">&gt; and also make it clear that it is the path expression, and not the
&gt; document, that determines whether the node test is testing an element name.</span >

Surely it's the user agent that determines whether the node test is testing an
element name?

I used &quot;the node&quot; because that is what XPath 1.0 section 2.3 Node Tests does
— it says &quot;A node test that is a QName is true if and only if the type of the
node [...]&quot; where &quot;the node&quot; has no referent.

Is there some other term I can use?


<span class="quote">&gt; Here's my best shot at this:
&gt; 
&gt; [...] namespace URI <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> (the HTML namespace)</span >

HTML5 style is to refer to the namespace as &quot;the HTML namespace&quot; with a
hyperlink to its definition, not to repeat the namespace wherever it occurs.


<span class="quote">&gt; when the node test occurs in a position where an element or type name is
&gt; expected</span >

This doesn't appear to use XPath 1.0 terminology. Do you mean &quot;when the node
test's principle node type is element&quot;? If so, isn't this redundant with saying
that the condition only applies when &quot;the node&quot; is an element?


<span class="quote">&gt; and the path expression is applied to a document that is an HTML document.</span >

As far as I can tell, this would miss nodes that are outside of the document
but whose owner document is an HTML document. It would also fail in the case
where a node is in a different document than its owner document (e.g. as in an
XBL shadow tree), though it may be that XPath doesn't support that today
anyway.


<span class="quote">&gt; I would also change the note, since this is no longer such a willful violation:</span >

It's exactly as much of a willful violation as before. We haven't actually
changed the implementation requirements at all relative to the text the spec
had last week, we've just rephrased it in a different way. It's still requiring
that implementations break XPath 1.0 requirements.

Please let me know if you still think the spec's current text (quoted aboved)
is inadequate.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c35" href="show_bug.cgi?id=7059#c35">#35</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-14 22:04:41</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >(In reply to <a href="show_bug.cgi?id=7059#c34">comment #34</a>)

<span class="quote">&gt; It has to say &quot;must&quot; otherwise there's no normative conformance criteria, and
&gt; it becomes impossible to determine if it's a statement trying to modify XPath,
&gt; or a statement trying to describe the results of other conformance criteria
&gt; (and failing).</span >

OK. I was trying to simplify the wording, you're right about keeping must, the
rest of this part is editorial. 

<span class="quote">&gt; &gt; and also make it clear that it is the path expression, and not the
&gt; &gt; document, that determines whether the node test is testing an element name.
&gt; 
&gt; Surely it's the user agent that determines whether the node test is testing an
&gt; element name?
&gt; 
&gt; I used &quot;the node&quot; because that is what XPath 1.0 section 2.3 Node Tests does
&gt; — it says &quot;A node test that is a QName is true if and only if the type of the
&gt; node [...]&quot; where &quot;the node&quot; has no referent.
&gt; 
&gt; Is there some other term I can use?</span >

You can look at a path expression and tell whether a node test will test
elements or not, you don't need a document to do that. The user agent may apply
a path expression to a document, but you don't need to do so to determine what
the path expression means.

You suggested &quot;when the node test's principle node type is element&quot; - that
works fine.

<span class="quote">&gt; &gt; Here's my best shot at this:
&gt; &gt; 
&gt; &gt; [...] namespace URI <a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a> (the HTML namespace)
&gt; 
&gt; HTML5 style is to refer to the namespace as &quot;the HTML namespace&quot; with a
&gt; hyperlink to its definition, not to repeat the namespace wherever it occurs.</span >

OK.

<span class="quote">&gt; &gt; when the node test occurs in a position where an element or type name is
&gt; &gt; expected
&gt; 
&gt; This doesn't appear to use XPath 1.0 terminology. Do you mean &quot;when the node
&gt; test's principle node type is element&quot;? If so, isn't this redundant with saying
&gt; that the condition only applies when &quot;the node&quot; is an element?</span >

&quot;when the node test's principle node type is element&quot; is fine. You don't have
&quot;the node&quot; until the path expression is applied to a document - and even then,
it might not be applied to a given node. I don't think it's a good idea to
define this in terms of the document to which it is applied, and that's
certainly not how XPath does it.

If you look at the XPath 1.0 spec, you'll see that principal node type is
defined in terms of the expression (with respect to its axes), not the document
that is tested.

<span class="quote">&gt; &gt; and the path expression is applied to a document that is an HTML document.
&gt; 
&gt; As far as I can tell, this would miss nodes that are outside of the document
&gt; but whose owner document is an HTML document. It would also fail in the case
&gt; where a node is in a different document than its owner document (e.g. as in an
&gt; XBL shadow tree), though it may be that XPath doesn't support that today
&gt; anyway.</span >

OK - leaving that part out is fine with me, and I like the semantics you
propose better.

<span class="quote">&gt; &gt; I would also change the note, since this is no longer such a willful violation:
&gt; 
&gt; It's exactly as much of a willful violation as before. We haven't actually
&gt; changed the implementation requirements at all relative to the text the spec
&gt; had last week, we've just rephrased it in a different way. It's still requiring
&gt; that implementations break XPath 1.0 requirements.
&gt; 
&gt; Please let me know if you still think the spec's current text (quoted aboved)
&gt; is inadequate.</span >

The NOTE is purely editorial, do what you wish with it.

I'll bring this up on the XML Query WG / XSL WG telcon tomorrow morning at
11:00 - 1:00 EST, and I'm pretty sure you would be welcome to join. I'll also
be available on IRC on the #xquery channel during working hours (again EST) if
it's helpful to chat.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c36" href="show_bug.cgi?id=7059#c36">#36</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-22 07:17:39</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" ><span class="quote">&gt; &gt; This doesn't appear to use XPath 1.0 terminology. Do you mean &quot;when the node
&gt; &gt; test's principle node type is element&quot;? If so, isn't this redundant with saying
&gt; &gt; that the condition only applies when &quot;the node&quot; is an element?
&gt; 
&gt; &quot;when the node test's principle node type is element&quot; is fine. You don't have
&gt; &quot;the node&quot; until the path expression is applied to a document - and even then,
&gt; it might not be applied to a given node. I don't think it's a good idea to
&gt; define this in terms of the document to which it is applied, and that's
&gt; certainly not how XPath does it.</span >

We don't have a choice here as far as I can see — surely we don't want these
changes applying outside of HTML documents.

I'm marking this fixed since it appears the text is adequate now; please feel
free to reopen it if there is still a problem.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c37" href="show_bug.cgi?id=7059#c37">#37</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2009-09-23 16:06:07</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >The XML Query and XSL Working Groups discussed this in our telcon yesterday,
and we suggest that you treat this as a modification of the following language
in XPath 1.0:

&lt;oldText&gt;
A QName in the node test is expanded into an expanded-name using the namespace
declarations from the expression context. This is the same way expansion is
done for element type names in start and end-tags except that the default
namespace declared with xmlns is not used: if the QName does not have a prefix,
then the namespace URI is null (this is the same way attribute names are
expanded). It is an error if the QName has a prefix for which there is no
namespace declaration in the expression context.
&lt;/oldText&gt;

Here is the text we suggest that you use. 

&lt;newText&gt;
A QName in the node test is expanded into an expanded-name using the namespace
declarations from the expression context. If the QName has a prefix, then there
must be namespace declaration for this prefix in the expression context, and
the correponding namespace URI is the one that is associated with this prefix.
It is an error if the QName has a prefix for
which there is no namespace declaration in the expression context. 

If the QName has no prefix and the principal node type of the axis is element,
then the default element namespace is used. Otherwise if the QName has no
prefix, the namespace URI is null. The default element namespace is a member of
the  context for the XPath expression. The value of the default element
namespace when executing an XPath expression through the DOM3 XPath API is
determined in the following way:

(1) If the context node is from an HTML DOM, the default element namespace is
&quot;<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot;.

(2) Otherwise, the default element namespace URI is null.

Note: This is equivalent to adding the default element namespace feature of
XPath 2.0 to XPath 1.0, and using the HTML namespace as the default element
namespace for HTML documents. It is motivated by the desire to have
implementations be compatible with legacy HTML content while still supporting
the changes that this specification introduces to HTML regarding the namespace
used for HTML elements, and by the desire to use XPath 1.0 rather than XPath
2.0.
&lt;/newText&gt;

Jonathan
(on behalf of the XML Query and XSL Working Groups)

</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c38" href="show_bug.cgi?id=7059#c38">#38</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:ian&#64;hixie.ch">Ian 'Hixie' Hickson</a>
        </span>

        2009-09-28 19:26:41</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Ok, I've checked in the above. Thanks!</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c39" href="show_bug.cgi?id=7059#c39">#39</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:contributor&#64;whatwg.org">contributor&#64;whatwg.org</a>
        </span>

        2009-09-28 19:26:49</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Checked in as WHATWG revision r4007.
Check-in comment: Rewrite how we patch XPath 1.0 for HTML5.
<a href="http://html5.org/tools/web-apps-tracker?from=4006&amp;to=4007">http://html5.org/tools/web-apps-tracker?from=4006&amp;to=4007</a></pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c40" href="show_bug.cgi?id=7059#c40">#40</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:mike&#64;w3.org">Michael(tm) Smith</a>
        </span>

        2009-10-05 04:36:09</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >Jonathan,

Can you please review the current text in the spec and confirm whether you (and
the XQuery and XSL WGs) are satisfied with it or if you want to request any
further changes to it. The section is here:

<a href="http://dev.w3.org/html5/spec/embedded-content-0.html#interactions-with-xpath-and-xslt">http://dev.w3.org/html5/spec/embedded-content-0.html#interactions-with-xpath-and-xslt</a> </pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c41" href="show_bug.cgi?id=7059#c41">#41</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:mjs&#64;apple.com">Maciej Stachowiak</a>
        </span>

        2010-03-14 14:48:20</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >This bug predates the HTML Working Group Decision Policy.

If you are satisfied with the resolution of this bug, please change the state
of this bug to CLOSED. If you have additional information and would like the
editor to reconsider, please reopen this bug. If you would like to escalate the
issue to the full HTML Working Group, please add the TrackerRequest keyword to
this bug, and suggest title and text for the tracker issue; or you may create a
tracker issue yourself, if you are able to do so. For more details, see this
document:
  <a href="http://dev.w3.org/html5/decision-policy/decision-policy.html">http://dev.w3.org/html5/decision-policy/decision-policy.html</a>

This bug is now being moved to VERIFIED. Please respond within two weeks. If
this bug is not closed, reopened or escalated within two weeks, it may be
marked as NoReply and will no longer be considered a pending comment.</pre>
    </div>
  <div class="bz_comment">

      <span class="bz_comment_head">
        <span class="comment_rule">-------</span>
        <i>Comment
        <a name="c42" href="show_bug.cgi?id=7059#c42">#42</a> From
        <span class="vcard">
          <a class="fn email" href="mailto:jonathan.robie&#64;redhat.com">Jonathan Robie</a>
        </span>

        2010-04-19 13:16:37</i>

        <span class="comment_rule">-------</span>
      </span>



<pre class="bz_comment_text" >I am happy with these changes.</pre>
    </div>
        </div>
        
      </td>
    </tr>
  </table>
</form>

<hr>
<ul class="related_actions">
    <li><a href="show_bug.cgi?format=multiple&amp;id=7059">Format For Printing</a></li>
    <li>&nbsp;-&nbsp;<a href="show_bug.cgi?ctype=xml&amp;id=7059">XML</a></li>
    <li>&nbsp;-&nbsp;<a href="enter_bug.cgi?cloned_bug_id=7059">Clone This Bug</a></li>
    
    <li>&nbsp;-&nbsp;<a href="#">Top of page </a></li>
    </ul>        


<div class="navigation">
  
  
  <i><font color="#777777">First</font></i>
  <i><font color="#777777">Last</font></i>
  <i><font color="#777777">Prev</font></i>
  <i><font color="#777777">Next</font></i>
  &nbsp;&nbsp;
  <i><font color="#777777">No search results available</font></i>
</div>

<br>
</div>



<div id="footer">
  <div class="intro"></div>




<ul id="useful-links">
  <li id="links-actions">
    <div class="label">Actions: </div><ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_bottom" name="quicksearch">
    <input class="btn" type="submit" value="Find" id="find_bottom"></form></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li></li>


      <li><span class="separator">| </span><a href="createaccount.cgi">New&nbsp;Account</a></li>
<li>
        <span class="separator">| </span>
        <a href="docs/html/bug_page.html" target="_blank">Help</a>
      </li>

      



      

        
      <li><span class="separator">| </span><a href="http://www.w3.org/Bugs/Public/show_bug.cgi?id=7059&amp;GoAheadAndLogIn=1">Log&nbsp;In</a></li>
</ul>
  </li>

  
    

  


  
</ul>

  <div class="outro"></div>
</div>

</body>
</html>