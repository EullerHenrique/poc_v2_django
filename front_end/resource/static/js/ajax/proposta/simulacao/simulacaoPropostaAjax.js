document.getElementById('botaoRealizarSimulacao').addEventListener('click', function(event){
  let endpoint = event.target.getAttribute('data-endpoint');
  let csrf_token = event.target.getAttribute('data-crsftoken');
  realizarSimulacaoProposta(endpoint, csrf_token);
});

document.getElementById('botaoGerarExcel').addEventListener('click', function(event){
  let endpoint = event.target.getAttribute('data-endpoint');
  let csrf_token = event.target.getAttribute('data-crsftoken');
  gerarExcelSimulacaoProposta(endpoint, csrf_token);
});

function realizarSimulacaoProposta(endpoint, csrf_token){
  if(validarCamposFormControl(document)){
    url = 'http://127.0.1:8001' + endpoint;
  
    response = fetch(url,{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({
        vlrSolicitado: document.getElementById('vlrSolicitado').value,
        vlrTAC: document.getElementById('vlrTAC').value?document.getElementById('vlrTAC').value:'0',
        tipoPessoa: document.getElementById('tipoPessoa').value,
        nroDiasAcrescimo: document.getElementById('nroDiasAcrescimo').value,
        percJurosNegociado: document.getElementById('percJurosNegociado').value
      })
     })
    .then(response =>{
      response_status = response.status;
      if(response_status == 401){
        window.location.href ='/auth/login';
      }else{
        return response.json();
      }
    })
    .then(json => {
        let parcelas = json.parcelas; 
       
        let resultadoSimulacao = document.getElementById('resultadoSimulacao');
        let table = document.getElementById('tabelaParcelas');
        let tbody = document.createElement('tbody');
        while (table.rows.length > 1) {
          table.deleteRow(1);
        }
        parcelas.forEach(parcela => {
          let tr = document.createElement('tr');
          let td = document.createElement('td');
          td.innerHTML = parcela.valorSolicitado;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.prazo;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrParcela;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrTAC;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrBoleto;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrSeguro;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrIOF;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.percIOF;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrTotalCredito;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.vlrTotalDivida;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.percCETMensal;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.percCETAnual;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.percJurosMensal;
          tr.appendChild(td);
          td = document.createElement('td');
          td.innerHTML = parcela.percJurosAnual;
          tr.appendChild(td);
          tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        resultadoSimulacao.style.display = "";
      })
    .catch(error => console.error(error))
  }
}       

function gerarExcelSimulacaoProposta(endpoint, csrf_token){
  if(validarCamposFormControl(document)){
    url = 'http://127.0.1:8001' + endpoint;
    response = fetch(url,{
      method: 'POST',
      headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({
        vlrSolicitado: document.getElementById('vlrSolicitado').value,
        vlrTAC: document.getElementById('vlrTAC').value?document.getElementById('vlrTAC').value:'0',
        tipoPessoa: document.getElementById('tipoPessoa').value,
        nroDiasAcrescimo: document.getElementById('nroDiasAcrescimo').value,
        percJurosNegociado: document.getElementById('percJurosNegociado').value
      })
    })
    .then(response =>{
      response_status = response.status;
      console.log(response_status);
      if(response_status == 403){
        return response.json();
      }else if(response_status == 401){
        window.location.href ='/auth/login';
      }else{
        return response.blob();
      }
    })
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      a.download = 'simulacao_proposta.xlsx';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error(error))
  }
}