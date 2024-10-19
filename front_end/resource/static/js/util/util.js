function validarCamposFormControl(document){
  let campoInvalido = false;
  for (let i = 0; i < document.getElementsByClassName('form-control').length; i++) {
    if (!document.getElementsByClassName('form-control')[i].classList.contains('form-optional')) {
      if (document.getElementsByClassName('form-control')[i].value == '') {
        campoInvalido = true;
        document.getElementsByClassName('form-control')[i].classList.add('is-invalid');
      }else{
        document.getElementsByClassName('form-control')[i].classList.remove('is-invalid');
      }
    }
  }
  if (campoInvalido) {
    exibirToastError('Preencha todos os campos!');
    return false;
  }
  return true;
}
  
function exibirToastError(msg){
    const toastHTML = `
    <div id="toast" class="m-3 position-fixed top-0 end-0" data-bs-animation="true" data-bs-autohide="true">
      <div class="toast text-bg-danger">
        <div class="d-flex">
          <div class="toast-body">
            ${msg}
          </div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>   
        </div> 
      </div>
    </div>
  `;
    if(document.querySelector('#toast')){
        document.querySelector('#toast').remove();
    }
    document.body.insertAdjacentHTML('beforeend', toastHTML);
    var toastEl = document.querySelector('.toast');
    var toast = new bootstrap.Toast(toastEl);
    toast.show();
  }

