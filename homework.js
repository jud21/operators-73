//Exercise #1
/*Write a function that takes in the string and the list of dog names, loops through 
the list and checks that the current name is in the string passed in. The output should be:
"Matched dog_name" if name is in the string, if no matches are present console.log "No Matches"
*/

let dog_string = "Hello Max, my name is Dog, and I have purple eyes!"
let dog_names = ["Max","HAS","PuRple","dog"]

let findWords = (string, list) =>{
    for(let i = 0; length(list); i++){
        if(list includes(string[5])){
            return 'Matched dog_name'
        }else{
            return 'No Matches'
        }
    }
};


//Exercise #2
//Write a function that takes in an array and removes every value that's double is over 50.
given_arr == [13, 22, 26, 40, 1, 10]

let removeOverFifty = (a_list) => {
    for(let i = 0; length(a_list); i++){
        if (i*2 > 50){
            a_list.splice(i){
    return a_list
            }
        }
    }
};


// Code Wars #1
//Multiply two inputs

function multiply(a, b){
    return a * b
  };


// Code Wars #2
//Convert boolean values to Strings.  True = 'Yes', False = 'No'

function boolToWord( bool ){
    if (bool) {
      return 'Yes';
    } else {
      return 'No';
    }
  };
