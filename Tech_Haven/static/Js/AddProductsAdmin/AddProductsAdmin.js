function check() {
    if (document.getElementsByName('file')[0].value == ''){
        document.getElementById('span_type').innerHTML = 'Please choose a file'
    }
    else if (document.getElementsByName('file')[0].value.slice(document.getElementsByName('file')[0].value.lastIndexOf('.')) != '.jpg' && document.getElementsByName('file')[0].value.slice(document.getElementsByName('file')[0].value.lastIndexOf('.')) != '.jpeg' && document.getElementsByName('file')[0].value.slice(document.getElementsByName('file')[0].value.lastIndexOf('.')) != '.png' && document.getElementsByName('file')[0].value.slice(document.getElementsByName('file')[0].value.lastIndexOf('.')) != '.gif'){
        document.getElementById('span_type').innerHTML = 'Please choose a correct file type (.jpg, .jpeg, .png, .gif)'
    }
    else {
        document.getElementById('span_type').innerHTML = '&nbsp;'
    }

    if (document.getElementsByName('product_id')[0].value == ''){
        document.getElementById('span_id').innerHTML = 'Please enter a Product ID'
    }
    else if (product_id_list.includes(document.getElementsByName('product_id')[0].value)){
        document.getElementById('span_id').innerHTML = 'This Product ID have already been registered'
    }
    else {
        document.getElementById('span_id').innerHTML = '&nbsp;'
    }

    if (document.getElementsByName('product_name')[0].value == ''){
        document.getElementById('span_name').innerHTML = 'Please enter a Product Name'
    }
    else {
        document.getElementById('span_name').innerHTML = '&nbsp;'
    }

    if (document.getElementsByName('product_description')[0].value == ''){
        document.getElementById('span_description').innerHTML = 'Please enter the Product Description'
    }
    else {
        document.getElementById('span_description').innerHTML = '&nbsp;'
    }

    if (document.getElementsByName('product_price')[0].value == ''){
        document.getElementById('span_price').innerHTML = 'Please enter the Product Price'
    }
    else if (document.getElementsByName('product_price')[0].value == '0'){
        document.getElementById('span_price').innerHTML = 'Product Price must be more than 0'
    }
    else {
        document.getElementById('span_price').innerHTML = '&nbsp;'
    }

    if (document.getElementsByName('form_name')[0].value == ''){
        document.getElementById('span_form_name').innerHTML = 'Please enter the Form Name'
    }
    else if (form_name_list.includes(document.getElementsByName('form_name')[0].value)){
        document.getElementById('span_form_name').innerHTML = 'This Form Name have already been registered'
    }
    else {
        document.getElementById('span_form_name').innerHTML = '&nbsp;'
    }


    if (document.getElementById('span_type').innerHTML == '&nbsp;' && document.getElementById('span_id').innerHTML == '&nbsp;' && document.getElementById('span_name').innerHTML == '&nbsp;' &&  document.getElementById('span_description').innerHTML == '&nbsp;' && document.getElementById('span_price').innerHTML == '&nbsp;' && document.getElementById('span_form_name').innerHTML == '&nbsp;'){
        alert('Product have been added.')
        document.getElementById('button').setAttribute("type", 'submit')
    }
}
