function showMenu(){
    document.getElementById("myProfileDropdown").classList.toggle("show");
    var img = document.getElementById("arrow1");
    img.style.transform = "rotate(180deg)";
}


window.onclick = function(event){
    if (!event.target.matches('.dropdownButton')){
        var dropdowns = document.getElementsByClassName("dropdownMenu");
        var i;
        for (i=0; i<dropdowns.length; i++){
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')){
                openDropdown.classList.remove('show');
            }
        }
        var img = document.getElementById("arrow1");
        img.style.transform =  "";
    }    
}

// ---------- new task ------------------------------------------------------------------------- */

function openNewTaksWindow() {
    document.getElementById("myForm").style.display = "block";
    document.getElementById("myForm").style.visibility = "visible";
  }
  
function closeNewTaskWindow() {
    document.getElementById("myForm").style.display = "none";
  }

// ---------- sidebar & hamburger menu --------------------------------------------------------- */

const menuBtn = document.querySelector(".menu-btn");
const sidebar = document.querySelector(".nav");
let menuOpen = false;
let siderbarOpen = false;
menuBtn.addEventListener("click", () => {
    if(!menuOpen) {
        menuBtn.classList.add("open");
        menuOpen = true;

        sidebar.classList.add("open");
        siderbarOpen = true;

    } else {
        menuBtn.classList.remove('open');
        menuOpen = false;

        sidebar.classList.remove("open");
        siderbarOpen = false;
    }
});

// ---------- small tasks dragging ------------------------------------------------------------- */

const smallTasks = document.querySelectorAll(".taskSmall");
const containers = document.querySelectorAll(".taskSectionSpan");

smallTasks.forEach(smallTask =>{
    smallTask.addEventListener("dragstart", () =>{
        smallTask.classList.add("smallTaskDragging");
    })

    smallTask.addEventListener("dragend", () =>{
        smallTask.classList.remove("smallTaskDragging");
    })
})

containers.forEach(container => {
    container.addEventListener("dragover", e => {
        e.preventDefault()
        const afterElement = getDragAfterElement(container, e.clientY);
        const drag = document.querySelector(".smallTaskDragging");
        if(afterElement == null){
            container.appendChild(drag)
        }
        else{
            container.insertBefore(drag, afterElement)
        }
    })
})

function getDragAfterElement(container, y){
    const draggableElements = [...container.querySelectorAll(".smallTask:not(.smallTaskDragging)")];

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect()
        const offset = y - box.top - box.height / 2
        if(offset < 0 && offset > closest.offset){
            return {offset: offset, element: child}
        }
        else{
            return closest
        } 
    }, {offset: Number.NEGATIVE_INFINITY}).element
}

// ---------- big task popup ------------------------------------------------------------------- */
/*
function createBigTask(e){
    const element = e.target.parentNode;
    const clone = element.cloneNode(true);
    document.body.appendChild(clone);
}*/
/*
const links = document.querySelectorAll(".smallToBig")

links.forEach(link => {
    link.addEventListener("click", () => {
        const elem = link.target.parentNode;
        const clone = elem.cloneNode(true);
        document.body.appendChild(clone);
    })
})
*/
function openBigTaskWindow() {
    document.getElementById("bigTaskWindow").style.display = "block";
    document.getElementById("bigTaskWindow").style.visibility = "visible";
  }
  
function closeBigTaskWindow() {
    document.getElementById("bigTaskWindow").style.display = "none";
  }

// ---------- sidebar temas dropdown ----------------------------------------------------------- */

var dropdown = document.getElementsByClassName("sidebarDropdownButton");
var i;

for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}

// ---------- switch between logging and registaration ----------------------------------------- */

// function switchToLog(){
//     document.getElementById("log").style.backgroundColor = "slategrey";
//     document.getElementById("reg").style.backgroundColor = "black";
//     document.getElementById("myForm").style.height = "50%";
// }
//
// function switchToReg(){
//     document.getElementById("log").style.backgroundColor = "black";
//     document.getElementById("reg").style.backgroundColor = "slategrey";
//     document.getElementById("myForm").style.height = "70%";
// }