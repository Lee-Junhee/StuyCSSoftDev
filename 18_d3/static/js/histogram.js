//Benjamin Avrahami, Junhee Lee
//SoftDev2 pd9, 1
//K18 :: Come Up For Air
//2020-04-06

var year = 2005;
const button = document.getElementById('button');
const heading = document.getElementById('heading');

render = function() {
    $.ajax({
        method: 'POST',
        url: '/data',
        data: {'year': year},
        sucess: function(raw) {
            data = []
            for (var key in raw) {
                data.append((key, raw[key]));
            }
            d3.select('.chart')
              .selectAll('div')
              .data(data)
              .join('div')
              .transition()
                .duration(1000)
                .style('width', d=> `${d[1]}px`)
                .text(d => d[0]);
            heading.innerHTML = `${year} SAT Scores by State`;
            button.innerHTML = 'Transition'
            year += 1;
        }
    });
}

button.addEventListener('click', render);