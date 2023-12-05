var messageId = 0;
var scripts = {};

function copyScript(preScriptBlockId)
{
  const preElement = document.getElementById(preScriptBlockId);
  const textToCopy = preElement.textContent;
  navigator.clipboard.writeText(textToCopy);
}

function runScript(resBlockId, localMessageId)
{
    script = scripts["#cmdResBlock" + localMessageId];
    const preElement = $.find('#preScriptBlock' + localMessageId);
    script = preElement[0].outerText

    $.ajax({
        url: "/api/run_command",
        type: "POST",
        dataType: "json",
        data: JSON.stringify({
          "command": script
        }),
        success: function(data) {
          console.log("Success:", data);
          response = data.response.replace(/\n/g,"<br/>");
          response = "<br/><span>" + 
          `<a href="#" style="color:blue" onclick="copyScript('preOutputBlock` + localMessageId + `')">
           <i class="bi bi-clipboard" style="color:black"></i></a>&nbsp;&nbsp;&nbsp;<b>Output</b></span>` 
           + "<pre id='preOutputBlock" + localMessageId + "'>" + response + "</pre>";

          $(resBlockId).prepend(response);
        },
        error: function(error) {
          console.error("Error:", error);
          $(resBlockId).prepend(error);
        }
      }); 
}

function insertBotTalk(chatsDivId, message, script)
{    
    scripts["#cmdResBlock" + messageId] = script;

    $(chatsDivId).prepend(
        `<div class="chat floatFix">
            <div class="chat-avatar">
                <h3><i class="bi bi-android" style="color:#337ab7"></i></h3>
            </div>
            <div class="chat-body">
                <div class="chat-content">
                    <p>
                        ` + message + `
                    </p>
                    <span style="color:blue">
                      <a href="#" style="color:blue" onclick="copyScript('preScriptBlock` + messageId + `')"><i class="bi bi-clipboard" style="color:black"></i></a>
                      &nbsp;
                      <a href="#" style="color:blue" onclick="runScript('#cmdResBlock` + messageId + `',` + messageId + `)">Run</a>                      
                    </span>
                    <div id="cmdResBlock` + messageId + `"/>
                </div>               
            </div>
           
        </div>`);
}

function insertUserTalk(chatsDivId, message)
{
    $(chatsDivId).prepend(
        `<div class="chat chat-left">
        <div class="chat-avatar">
            <h2><i class="bi bi-person" style="color:#337ab7"></i></h2>
        </div>
        <div class="chat-body">
            <div class="chat-content">
                <p>` + message+ `</p>
            </div>
        </div>
    </div>`);
}

$( "#btnSend" ).on( "click", function(event) {
    cmd = $("#txtCmd").val();
    $("#txtCmd").val('')
    $("#txtCmd").focus()

    if(!cmd) return;
    insertUserTalk("#idChatContainer", cmd); 

    $.ajax({
        url: "/api/user_command",
        type: "POST",
        dataType: "json",
        data: JSON.stringify({
          "command": cmd
        }),
        success: function(data) {
          messageId++;
          console.log("Success:", data);
          response = data.response.replace(/\n/g,"<br/>");
          response = response.replace(/Low Risk/g,"<b><span style='color:green'>Low Risk</span></b>");
          response = response.replace(/High Risk/g,"<b><span style='color:red'>High Risk</span></b>");
          response += "<br/><i class='bi bi-pen' style='color:blue'></i></b> &nbsp;Editable Script<pre id='preScriptBlock" + messageId + "' contenteditable='true'>" + data.script + "</pre>";
          insertBotTalk("#idChatContainer", response, data.script);
        },
        error: function(error) {
          messageId++;
          console.error("Error:", error);
          insertBotTalk("#idChatContainer",error);
        }
      });          
});

$(document).ready(function() {
    $('#txtCmd').keypress(function(event) {
      if (event.keyCode === 13) {
        event.preventDefault();
        $('#btnSend').trigger('click');        
      }
    });
  })