function check() {
    if (document.getElementById('first_name').value == ''){
        document.getElementById('span_first_name').innerHTML = 'Please enter your first name'
    }
    else {
        document.getElementById('span_first_name').innerHTML = '&nbsp;'
    }

    if (document.getElementById('last_name').value == ''){
        document.getElementById('span_last_name').innerHTML = 'Please enter your last name'
    }
    else {
        document.getElementById('span_first_name').innerHTML = '&nbsp;'
    }

    if (document.getElementById('password').value == ''){
        document.getElementById('span_password').innerHTML = 'Please enter a password'
    }
    else if (document.getElementById('password').value.length < 8>){
        document.getElementById('span_password').innerHTML = 'The password must have at least 8 characters'
    }
    else {
        document.getElementById('span_password').innerHTML = '&nbsp;'
    }

    if (document.getElementById('confirm').value == ''){
        document.getElementById('span_confirm').innerHTML = 'Please re-enter your password'
    }
    else {
        document.getElementById('span_confirm').innerHTML = '&nbsp;'
    }

    if (document.getElementById('password').value != document.getElementById('confirm').value){
        document.getElementById('span_password').innerHTML = 'The password does not match. Please try again.'
        document.getElementById('confirm').innerHTML = 'The password does not match. Please try again.'
    }
    else {
        document.getElementById('span_confirm').innerHTML = '&nbsp;'
    }

    if (document.getElementById('street').value == ''){
        document.getElementById('span_street').innerHTML = 'Please enter your street name'
    }
    else {
        document.getElementById('span_first_name').innerHTML = '&nbsp;'
    }




    if (document.getElementById('span_password').innerHTML == '&nbsp;' && document.getElementById('span_id').innerHTML == '&nbsp;' && document.getElementById('span_name').innerHTML == '&nbsp;' &&  document.getElementById('span_description').innerHTML == '&nbsp;' && document.getElementById('span_price').innerHTML == '&nbsp;' && document.getElementById('span_form_name').innerHTML == '&nbsp;'){
        document.getElementById('button').setAttribute("type", 'submit')
    }
}
