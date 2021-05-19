var messages;

const msgs_div = document.getElementById('msgs');

function check() {
    var url = window.origin + "/chat/latest_msgs/" + chatwith;
    $.get(url, function(data, status) {
        if (data) {
            msgs = data;
            for (var i = 0; i < data.length; i++) {
                if (document.getElementById('message' + msgs[i].pk) == null) {
                    var d = new Date(msgs[i].fields["date_postdate"]);
                    if (msgs[i].fields['msg_from'] == chatwith) {
                        var div = document.createElement('div');
                        div.className = 'recevied-chats';
                        div.id = 'message' + msgs[i].pk;
                        div.innerHTML = '<div class="recevied-msg"><div class="recevied-msg-inbox"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div></div>';
                        msgs_div.appendChild(div);
                        msgs_div.scrollTop = msgs_div.scrollHeight;
                    } else {
                        var div = document.createElement('div');
                        div.className = 'outgoing-chats';
                        div.id = 'message' + msgs[i].pk;
                        div.innerHTML = '<div class="outgoing-chats-msg"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div>';
                        msgs_div.appendChild(div);
                        msgs_div.scrollTop = msgs_div.scrollHeight;
                    }
                }
            }
        }
    });
}

function display(msgs) {
    for (var i = 0; i < msgs.length; i++) {
        var d = new Date(msgs[i].fields["date_postdate"]);
        if (msgs[i].fields['msg_from'] == chatwith) {
            var div = document.createElement('div');
            div.className = 'recevied-chats';
            div.id = 'message' + msgs[i].pk;
            div.innerHTML = '<div class="recevied-msg"><div class="recevied-msg-inbox"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div></div>';
            // msgs_div.innerHTML('<div class="recevied-chats"><div class="recevied-msg"><div class="recevied-msg-inbox"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div></div></div>');
            msgs_div.appendChild(div);
        } else {
            var div = document.createElement('div');
            div.className = 'outgoing-chats';
            div.id = 'message' + msgs[i].pk;
            div.innerHTML = '<div class="outgoing-chats-msg"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div>';
            msgs_div.appendChild(div);
            // msgs_div.appendChild('<div class="outgoing-chats"><div class="outgoing-chats-msg"><p>' + msgs[i].fields['msg_text'] + '</p><span class="time">' + d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + '</span></div></div>');
        }
    }
}


function onPageLoad() {
    var url = window.origin + "/chat/msgs/" + chatwith;
    $.get(url, function(data, status) {
        if (data) {
            messages = data;
            display(messages);
            msgs_div.scrollTop = msgs_div.scrollHeight;
        }
    });
}

window.onload = onPageLoad;

var myVar = setInterval(check, 2000);
