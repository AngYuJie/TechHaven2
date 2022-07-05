var format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?~1234567890]/
var special_characters = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?~]/

function check() {
    if (document.getElementById('first_name').value == ''){
        document.getElementById('span_first_name').innerHTML = 'Please enter your first name'
    }
    else if(format.test(document.getElementById('first_name').value)){
        document.getElementById('span_first_name').innerHTML = 'Please enter a valid first name'
    }
    else {
        document.getElementById('span_first_name').innerHTML = '&nbsp;'
    }

    if (document.getElementById('last_name').value == ''){
        document.getElementById('span_last_name').innerHTML = 'Please enter your last name'
    }
    else if(format.test(document.getElementById('last_name').value)){
        document.getElementById('span_last_name').innerHTML = 'Please enter a valid last name'
    }
    else {
        document.getElementById('span_last_name').innerHTML = '&nbsp;'
    }

    if (document.getElementById('password').value == ''){
        document.getElementById('span_password').innerHTML = 'Please enter a password'
    }
    else if (document.getElementById('password').value.length < 8){
        document.getElementById('span_password').innerHTML = 'Password must have at least 8 characters'
    }
    else if (special_characters.test(document.getElementById('password').value) == false){
        document.getElementById('span_password').innerHTML = 'Password must have at least 1 special characters'
    }
    else if (document.getElementById('password').value != document.getElementById('confirm').value && document.getElementById('confirm').value != ''){
        document.getElementById('span_password').innerHTML = 'The password does not match. Please try again.'
    }
    else {
        document.getElementById('span_password').innerHTML = '&nbsp;'
    }

    if (document.getElementById('password').value == '' && document.getElementById('confirm').value == ''){
        document.getElementById('span_confirm').innerHTML = '&nbsp;'
    }
//    else if (document.getElementById('confirm').value != '' && document.getElementById('confirm').value.length < 8){
//        document.getElementById('span_confirm').innerHTML = 'Password must have at least 8 characters'
//    }
    else if (document.getElementById('password').value != ''&& document.getElementById('confirm').value == ''){
        document.getElementById('span_confirm').innerHTML = 'Please re-enter your password'
    }
    else if (document.getElementById('password').value != document.getElementById('confirm').value){
        document.getElementById('span_confirm').innerHTML = 'The password does not match. Please try again.'
    }
    else {
        document.getElementById('span_confirm').innerHTML = '&nbsp;'
    }

    if (document.getElementById('street').value == ''){
        document.getElementById('span_street').innerHTML = 'Please enter your street name'
    }
    else {
        document.getElementById('span_street').innerHTML = '&nbsp;'
    }

    if (document.getElementById('postal_code').value == ''){
        document.getElementById('span_postal_code').innerHTML = 'Please enter your postal code'
    }
    else if (document.getElementById('postal_code').value.length != 6){
        document.getElementById('span_postal_code').innerHTML = 'Please enter a valid postal code'
    }
    else if (isNaN(document.getElementById('postal_code').value)){
        document.getElementById('span_postal_code').innerHTML = 'Please enter a valid postal code'
    }
    else if (document.getElementById('postal_code').value == '000000'){
        document.getElementById('span_postal_code').innerHTML = 'Please enter a valid postal code'
    }
    else {
        document.getElementById('span_postal_code').innerHTML = '&nbsp;'
    }

    if (document.getElementById('unit_number').value == ''){
        document.getElementById('span_unit_number').innerHTML = 'Please enter your unit number'
    }
    // unit number length can be up to #00-0000, minimum #00-00
    else if (document.getElementById('unit_number').value.length > 8 ||document.getElementById('unit_number').value.length < 5){
        document.getElementById('span_unit_number').innerHTML = 'Please enter a valid unit number'
    }
    else if (document.getElementById('unit_number').value.slice(0,1) != '#'){
        document.getElementById('span_unit_number').innerHTML = 'Please follow the correct format (#00-00)'
    }
    else if (isNaN(document.getElementById('unit_number').value.slice(1,3))){
        document.getElementById('span_unit_number').innerHTML = 'Please enter a valid unit number'
    }
    else if (document.getElementById('unit_number').value.slice(3,4) != '-'){
        document.getElementById('span_unit_number').innerHTML = 'Please follow the correct format (#00-00)'
    }
    else if (document.getElementById('unit_number').value.slice(3,4) != '-'){
        document.getElementById('span_unit_number').innerHTML = 'Please follow the correct format (#00-00)'
    }
    else if (isNaN(document.getElementById('unit_number').value.slice( document.getElementById('unit_number').value.indexOf('-') ))){
        document.getElementById('span_unit_number').innerHTML = 'Please enter a valid unit number'
    }
    else {
        document.getElementById('span_unit_number').innerHTML = '&nbsp;'
    }

    if (document.getElementById('mobile_number').value == ''){
        document.getElementById('span_mobile_number').innerHTML = 'Please enter your mobile number'
    }
    else if (document.getElementById('mobile_number').value.length != 8){
        document.getElementById('span_mobile_number').innerHTML = 'Please enter a valid mobile number'
    }
    else if (isNaN(document.getElementById('mobile_number').value)){
        document.getElementById('span_mobile_number').innerHTML = 'Please enter a valid mobile number'
    }
    else {
        document.getElementById('span_mobile_number').innerHTML = '&nbsp;'
    }

        // check email
    if (document.getElementById('email').value == ''){
        document.getElementById('span_email').innerHTML = 'Please enter your email'
    }
        // check if there are '@' in email
    else if (!document.getElementById('email').value.includes('@')){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // check if there are 2 '@' in email
    else if (document.getElementById('email').value.indexOf('@') != document.getElementById('email').value.lastIndexOf('@')){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // check if there is any spacing in email
    else if (document.getElementById('email').value.includes(' ')){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // check if there are any letters between '@' and '.' in the domain section
    else if (document.getElementById('email').value.slice(document.getElementById('email').value.indexOf('@')+1, document.getElementById('email').value.lastIndexOf('.')) == ''){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // check if there are any letters after '.' in the domain section
    else if (document.getElementById('email').value.slice(document.getElementById('email').value.lastIndexOf('.')+1) == '' ){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // ensure no numbers and special characters between '@' and '.' in domain section
    else if(format.test(document.getElementById('email').value.slice(document.getElementById('email').value.indexOf("@")+1, document.getElementById('email').value.lastIndexOf('.')))){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
        // ensure no numbers and special characters after '.' in domain section
    else if(format.test(document.getElementById('email').value.slice(document.getElementById('email').value.lastIndexOf('.')+1))){
        document.getElementById('span_email').innerHTML = 'Invalid email address'
    }
    else{
        document.getElementById('span_email').innerHTML = '&nbsp;'
    }


    if (document.getElementById('span_first_name').innerHTML == '&nbsp;' && document.getElementById('span_last_name').innerHTML == '&nbsp;' && document.getElementById('span_password').innerHTML == '&nbsp;' &&  document.getElementById('span_confirm').innerHTML == '&nbsp;' && document.getElementById('span_street').innerHTML == '&nbsp;' && document.getElementById('span_postal_code').innerHTML == '&nbsp;' && document.getElementById('span_unit_number').innerHTML == '&nbsp;' && document.getElementById('span_mobile_number').innerHTML == '&nbsp;' && document.getElementById('span_email').innerHTML == '&nbsp;'){
        document.getElementById('button').setAttribute("type", 'submit')
    }
}
