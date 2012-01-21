$(document).ready(function() {
    var tn3 = $('.tn3gallery').tn3({
        skinDir:'css',
        imageClick:'fullscreen',
        image:{
            maxZoom:2.0,
            crop:true,
            clickEvent:'dblclick',
            transitions:[{
                type:'blinds'
            },{
                type:'grid'
            },{
                type:'grid',
                duration:350,
                easing:'easeInQuad',
                gridX:1,
                gridY:8,
                // flat, diagonal, circle, random
                sort:'random',
                sortReverse:false,
                diagonalStart:'bl',
                // fade, scale
                method:'scale',
                partDuration:360,
                partEasing:'easeOutSine',
                partDirection:'left'
            }]
        }
    });
});