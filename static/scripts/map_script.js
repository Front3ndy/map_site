'use strict'

const tabItem = document.querySelectorAll('.tab-item__btn');
const tabContent = document.querySelectorAll('.folium-map');

tabItem.forEach(function(el){
    el.addEventListener('click', open);
});

function open(evt){
    const tabTarget = evt.currentTarget;
    const button = tabTarget.dataset.button;

    tabItem.forEach(function(item){
        item.classList.remove('tab-item__btn-active');
    });

    tabContent.forEach(function(item){
        item.classList.remove('folium-map-active');
    });

    tabTarget.classList.add('tab-item__btn-active');
    document.querySelector(`#${button}`).classList.add('folium-map-active');
}