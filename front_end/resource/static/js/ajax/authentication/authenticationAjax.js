document.getElementById('formLogin').addEventListener('submit', function(event){
  event.preventDefault();
  let endpoint = event.target.getAttribute('data-endpoint');
  let csrf_token = event.target.getAttribute('data-crsftoken');
  realizarLogin(endpoint, csrf_token);
});

function realizarLogin(endpoint, csrf_token){
  if(validarCamposFormControl(document)){
      url = 'http://127.0.1:8001' + endpoint;
      response = fetch(url,{
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
          },
          body: JSON.stringify({
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
          })
       })
      .then(response =>{
        response_status = response.status;
        if(response_status == 200){
          window.location.href ='/';
        }else if(response_status == 401){
          return response.json();
        }
      })
      .then(json => {
        exibirToastError(json.message);
      })
      .catch(error => console.error(error))
    }
}       