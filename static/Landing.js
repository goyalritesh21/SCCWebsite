const SID_re = /^[0-9]{8,8}$/;
function validate_SID( SID ) {
    console.log(SID);
    if(SID.match(SID_re)){
        return true;
    }
    return false;
}

const Mob_re = /^[0-9]{10,10}$/;
function validate_Mob( mobile ) {
    console.log(mobile);
    if(mobile.match(Mob_re)){
        return true;
    }
    return false;
}

const url = 'http://127.0.0.1:5000/'

function validate_form(form) {
    let msg = "";
    if(validate_SID(form.SID.value) !== true){
        msg = msg + "SID invalid\n";
    }
    if(validate_Mob(form.Mobile.value) !== true){
        msg = msg + "Mobile Number invalid\n";
    }
    if(msg.length > 0){
        alert(msg);
        form.reset();
        return false;
    }
    else{
        console.log("Data sent");
        return true;
    }
}