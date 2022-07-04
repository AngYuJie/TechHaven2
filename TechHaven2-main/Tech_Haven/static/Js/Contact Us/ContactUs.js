var format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,<>\/?~1234567890]/


function check(){
    // check name
    if (document.getElementById('first_name').value == ''){
        document.getElementById('FirstNameSpan').innerHTML = 'Please enter your first name'
    }
    else{
        document.getElementById('FirstNameSpan').innerHTML = '&nbsp;'
    }

    if (document.getElementById('last_name').value == ''){
        document.getElementById('LastNameSpan').innerHTML = 'Please enter your last name'
    }
    else{
        document.getElementById('LastNameSpan').innerHTML = '&nbsp;'
    }



    // check email
    if (document.getElementById('email').value == ''){
        document.getElementById('EmailSpan').innerHTML = 'Please enter your email'
    }
        // check if there are '@' in email
    else if (!document.getElementById('email').value.includes('@')){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
        // check if there are 2 '@' in email
    else if (document.getElementById('email').value.indexOf('@') != document.getElementById('email').value.lastIndexOf('@')){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
        // check if there is any spacing in email
    else if (document.getElementById('email').value.includes(' ')){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }

        // check if there are any letters between '@' and '.' in the domain section
    else if (document.getElementById('email').value.slice(document.getElementById('email').value.indexOf('@')+1, document.getElementById('email').value.lastIndexOf('.')) == ''){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
        // check if there are any letters after '.' in the domain section
    else if (document.getElementById('email').value.slice(document.getElementById('email').value.lastIndexOf('.')+1) == '' ){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
        // ensure no numbers and special characters between '@' and '.' in domain section
    else if(format.test(document.getElementById('email').value.slice(document.getElementById('email').value.indexOf("@")+1, document.getElementById('email').value.lastIndexOf('.')))){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
        // ensure no numbers and special characters after '.' in domain section
    else if(format.test(document.getElementById('email').value.slice(document.getElementById('email').value.lastIndexOf('.')+1))){
        document.getElementById('EmailSpan').innerHTML = 'Invalid email address'
    }
    else{
        document.getElementById('EmailSpan').innerHTML = '&nbsp;'
    }


    // check subject
        if (document.getElementById('subject').value == ''){
            document.getElementById('SubjectSpan').innerHTML = 'Please enter a subject'
        }
        else{
            document.getElementById('SubjectSpan').innerHTML = '&nbsp;'
        }
    // check remarks
    if (document.getElementById('inquiry').value == ''){
        document.getElementById('InquirySpan').innerHTML = 'Please enter your inquiry'
    }
    else{
        document.getElementById('InquirySpan').innerHTML = '&nbsp;'
    }


    // if no error, then will be able to submit
    if (document.getElementById('FirstNameSpan').innerHTML == '&nbsp;' && document.getElementById('LastNameSpan').innerHTML == '&nbsp;' && document.getElementById('EmailSpan').innerHTML == '&nbsp;' &&  document.getElementById('SubjectSpan').innerHTML == '&nbsp;' && document.getElementById('InquirySpan').innerHTML == '&nbsp;'){
        alert('Thank You for submitting the form. You will now be sent back to the home page')
        document.getElementById('button').setAttribute("type", 'submit')
    }
}

