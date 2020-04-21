// document.addEventListener('DOMContentLoaded' , () =>{
//     document.querySelector('#form').onsubmit = () => {
//         const request = new XMLHttpRequest();
//         const name = document.querySelector('#name_entered').value;
//         request.open('POST','/hello');
//         request.onload = () => {
//             const data = JSON.parse(request.responseText);
//             if (data.success) {
//                 const contents = data.da;
//                 document.querySelector('#result').innerHTML = contents;
//             }
//             else{
//                 document.querySelector('#result').innerHTML = 'There was an error';
//             }
//         }
//         const data = new FormData();
//         data.append('name_entered',name);
//         request.send(data);
//         return false;
//     };
// });