function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('lol');
    }, 200);
  });
}

export default getResponseFromAPI;
