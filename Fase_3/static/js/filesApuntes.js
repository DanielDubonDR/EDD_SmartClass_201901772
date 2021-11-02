const dropArea = document.querySelector(".drop-area");
const dragText = dropArea.querySelector("h2");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("#input-file");
let files;

button.addEventListener("click", (e) => {
    input.click();
});

input.addEventListener("change", (e) => {
    files = this.files;
    dropArea.classList.add("active");
    showFiles(files);
    dropArea.classList.remove("active");
});

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Suelta para subir el archivo";
});

dropArea.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra y suelta el archivo";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    files = e.dataTransfer.files;
    showFiles(files);
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra y suelta el archivo";
});


function showFiles(files){
    if(files.length === undefined)
    {
        processFile(files);
    }
    else
    {
        for(const file of files)
        {
            processFile(file);
        }
    }
}

function processFile(file)
{
    const docType = file.type;
    const validExtensions = ['text/plain', 'application/json'];

    if(validExtensions.includes(docType))
    {
        const fileReader = new FileReader();
        const id = `file-${Math.random().toString(32).substring(7)}`;

        fileReader.addEventListener('load', e =>{
            const fileUrl = fileReader.result;
            const text = `
            <div id="${id}" class="file-container">
                <div class="status">
                    <span>${file.name}</span>
                    <span class="status-text" id="ad">
                        Loading...
                    </span>
                </div>
            </div>
            `;
            const html = document.querySelector("#preview").innerHTML;
            document.querySelector("#preview").innerHTML = text + html;
            upload(fileUrl);
        });
        fileReader.readAsText(file);
    }
    else
    {
        alert('Archivo no valido');
    }
}

function upload(data){
    // console.log(objeto);
    fetch('/loadApuntes', 
    { method: 'POST', body: data, headers:{ 'Content-Type': 'application/json'}}).then(res => res.json())
    .catch(error => { 
        console.error('Error:', error)
        alert("Ocurrio un error")
        document.querySelector("#ad").innerHTML = `<span class="failure">El archivo no pudo subirse ...</span>`;
    })
    .then(response =>{
        console.log('Success:', response);
        if(response.Mensaje == true)
        {
            document.querySelector("#ad").innerHTML = `<span class="success">Archivo subido correctamente ...</span>`;
        }
    }) 
}