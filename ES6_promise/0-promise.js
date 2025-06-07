function  getResponseFromAPI(){
    return new Promise((resolve, reject) => {
	setTimeout(() => {
	    resolve("lol");
	}, 200);
    });
};

export default getResponseFromAPI;
