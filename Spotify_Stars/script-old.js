// select all elements with the 'i' tag and store them in a Nodelist called 'stars'                           
const stars = document.querySelectorAll(".stars i");                                                          
                                                                                                              
// //Loop through the 'stars' NodeList                                                                        
stars.forEach((star, index1) => {                                                                             
    //add an event listener that runs a function when the 'click' event is triggered                          
    star.addEventListener("click",()=> {                                                                      
        console.log(index1);                                                                                  
        // //Loop through the 'stars' NodeList again                                                          
        stars.forEach((star,index2) => {                                                                      
            //Add the "active" class to the clicked star and any stars with a lower index                     
          //and remove the "active" class from any stars with a higher index                                  
          console.log(index1,index2);                                                                         
          if (index2 >= (Math.trunc(index1/5)*5) && index2 < (Math.trunc((index1+5)/5)*5)) {                  
            index2 <= index1 ? star.classList.add("active") : star.classList.remove("active");                
          }                                                                                                   
        });                                                                                                   
                                                                                                              
    });                                                                                                       
});                                                                                                           
