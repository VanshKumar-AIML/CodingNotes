/* =========================================================
   DNA HELIX GENERATION SCRIPT
========================================================= */

// DOM elements
const dna = document.getElementById("dna");
const pairsSlider = document.getElementById("pairs");
const heightSlider = document.getElementById("height");
const radiusSlider = document.getElementById("radius");
const twistSlider = document.getElementById("twist");
const speedSlider = document.getElementById("speed");

// Value displays
const pairsVal = document.getElementById("pairsVal");
const heightVal = document.getElementById("heightVal");
const radiusVal = document.getElementById("radiusVal");
const twistVal = document.getElementById("twistVal");
const speedVal = document.getElementById("speedVal");

// Default parameters
let totalPairs = parseInt(pairsSlider.value);
let helixHeight = parseInt(heightSlider.value);
let helixRadius = parseInt(radiusSlider.value);
let twist = parseInt(twistSlider.value);
let speed = parseInt(speedSlider.value);

/* ---------------------------------------------------------
   Build DNA Structure
--------------------------------------------------------- */
function buildDNA() {
  dna.innerHTML = "";

  const stepY = helixHeight / totalPairs;

  for (let i = 0; i < totalPairs; i++) {
    const base = document.createElement("div");
    base.className = "base";

    const dotA = document.createElement("div");
    dotA.className = "dot a";

    const dotB = document.createElement("div");
    dotB.className = "dot b";

    const link = document.createElement("div");
    link.className = "link";

    base.appendChild(dotA);
    base.appendChild(link);
    base.appendChild(dotB);

    const y = -helixHeight / 2 + i * stepY;
    const angle = i * twist;

    base.style.transform =
      `rotateY(${angle}deg) translateZ(${helixRadius}px) translateY(${y}px)`;

    dna.appendChild(base);
  }
}

/* ---------------------------------------------------------
   Update Speed
--------------------------------------------------------- */
function updateSpeed() {
  dna.style.animationDuration = speed + "s";
}

/* ---------------------------------------------------------
   Event Listeners
--------------------------------------------------------- */
pairsSlider.addEventListener("input", () => {
  totalPairs = parseInt(pairsSlider.value);
  pairsVal.textContent = totalPairs;
  buildDNA();
});

heightSlider.addEventListener("input", () => {
  helixHeight = parseInt(heightSlider.value);
  heightVal.textContent = helixHeight;
  buildDNA();
});

radiusSlider.addEventListener("input", () => {
  helixRadius = parseInt(radiusSlider.value);
  radiusVal.textContent = helixRadius;
  buildDNA();
});

twistSlider.addEventListener("input", () => {
  twist = parseInt(twistSlider.value);
  twistVal.textContent = twist;
  buildDNA();
});

speedSlider.addEventListener("input", () => {
  speed = parseInt(speedSlider.value);
  speedVal.textContent = speed + "s";
  updateSpeed();
});

/* ---------------------------------------------------------
   Initialize
--------------------------------------------------------- */
buildDNA();
updateSpeed();

const items = document.querySelectorAll('.ring-item');
const radius = 120;
let angle = 0;

function animate() {
  angle += 0.01;

  items.forEach((item, i) => {
    const total = items.length;
    const theta = angle + (i * (2 * Math.PI / total));
    const x = radius * Math.cos(theta);
    const y = radius * Math.sin(theta);
    const z = Math.sin(theta); // depth illusion

    const scale = 0.5 + 0.5 * (z + 1) / 2; // range: 0.5 to 1
    const yOffset = z * 40; // positive = rise, negative = drop

    item.style.transform = `
      translateX(${x}px)
      translateY(${yOffset}px)
      scale(${scale})
    `;
    item.style.zIndex = Math.round(scale * 100); // layering
    item.style.opacity = scale; // subtle fade
  });

  requestAnimationFrame(animate);
}

animate();

/*function getdata(dataid,getnextdata){
  setTimeout(()=>{
    console.log("data",dataid);
    if(getnextdata){
     getnextdata();
    }       
  },2000);
}
//nested callbacks
getdata(1, () => {
  console.log("getting data 2......")
            getdata(2,()=>{
              console.log("getting data 3.....");
              getdata(3,()=>{
                console.log("getting data 4.....");
                getdata(4,()=>{
                  console.log("getting data 5.....");
                  getdata(5);
  
                });
              });
            });
 });

//promises
let promise= new Promise((resolve,reject)=>{
  console.log("promise");
  reject("some error");
});  */

function async1(){
  return new Promise((resolve,reject) => {
    setTimeout( ()=>{
      console.log("data1");
      resolve("success");
    },3000);
  });
}

function async2(){
  return new Promise((resolve,reject) => {
    setTimeout( ()=>{
      console.log("data2");
      resolve("success");
    },4000);
  });
}

console.log("getting or fetching data1");
let p1=async1();
p1.then((res) =>{
  console.log(res);
  console.log("getting or fetching data2");
  let p2=async2();
  p2.then((res) =>{
    console.log(res);
  });
});
