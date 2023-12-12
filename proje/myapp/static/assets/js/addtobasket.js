window.onload =function(){

    const items =localStorage.getItem('urunler')

    if (!items && items ==null) {
        
        localStorage.setItem("urunler", "[]")
    }
}

window.onload = function () {
    // LocalStorage'tan ürünleri alma
    let urunler = JSON.parse(localStorage.getItem('urunler'));

    if (!urunler) {
        // Eğer ürünler henüz tanımlanmamışsa, boş bir dizi olarak tanımla
        urunler = [];
        localStorage.setItem('urunler', JSON.stringify(urunler));
    }
}

async function HandleAddBasket(id) {
    // API'den ürünü al
    const request = await fetch(`http://127.0.0.1:8000/api/urun/${id}`);
    const response = await request.json();

    // Eğer ürün bulunamadıysa
    if (response === "ürün bulunamadı") {
        alert("Ürün bulunamadı.");
        return;
    }

    console.log('Gelen veri: ', response);

    // Ürünü JSON formatına çevir
    const model = JSON.stringify(response);

    // Sepeti LocalStorage'tan al
    let urunler = JSON.parse(localStorage.getItem('urunler'));

    // Ürünü sepete ekle
    urunler.push(model);

    // Sepeti güncelle ve LocalStorage'a kaydet
    localStorage.setItem('urunler', JSON.stringify(urunler));

    alert("Ürününüz sepete eklendi.");
}
