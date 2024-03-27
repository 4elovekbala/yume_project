export const getNameFromId = (id, products) => {
   let idToNames = {};

   for(let i = 0; i < products.length; i++){
      idToNames[products[i].id] = products[i].name
   } 
      
   return `${idToNames[id]} `
}