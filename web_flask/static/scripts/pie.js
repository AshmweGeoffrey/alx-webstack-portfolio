const data = JSON.parse(document.getElementById('exo').textContent.replace(/'/g, '"'));
        const labels = Object.keys(data);
        const values = Object.values(data);
        const ctx = document.getElementById('myPieChart').getContext('2d');
        const myPieChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    label: 'My Dataset',
                    data: values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.label + ': ' + context.raw;
                            }
                        }
                    }
                }
            }
        });
        // line pointing at the pie chart
function updatePositions() {
    const totSales = document.getElementById('tot-sales');
    const pie = document.getElementById('pie');

    const totSalesRect = totSales.getBoundingClientRect();
    const pieRect = pie.getBoundingClientRect();

    const svg = document.getElementById('svg');
    svg.innerHTML = ''; // Clear the previous elements

    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', totSalesRect.right);
    line.setAttribute('y1', totSalesRect.top + totSalesRect.height / 2);
    line.setAttribute('x2', pieRect.left);
    line.setAttribute('y2', pieRect.top + pieRect.height / 2);
    line.style.stroke = 'rgb(0,128,0)'; // Set the line color to green
    line.style.strokeWidth = '1.5'; // Set the line width to 1.5px
    line.setAttribute('marker-end', 'url(#arrow)'); // Add an arrow to the end of the line

    const marker = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
    marker.setAttribute('id', 'arrow');
    marker.setAttribute('markerWidth', '10');
    marker.setAttribute('markerHeight', '10');
    marker.setAttribute('refX', '0');
    marker.setAttribute('refY', '3');
    marker.setAttribute('orient', 'auto');
    marker.setAttribute('markerUnits', 'strokeWidth');
    marker.innerHTML = '<path d="M0,0 L0,6 L9,3 z" fill="#008000" />'; // The arrow shape

    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', (totSalesRect.right + pieRect.left) / 2); // Position the text over the line
    text.setAttribute('y', ((totSalesRect.top + pieRect.top) / 2) - 10); // Position the text 10px above the line
    text.style.fill = 'rgb(255,0,0)'; // Set the text color to red

    svg.appendChild(marker);
    svg.appendChild(line);
    svg.appendChild(text);
}

window.onload = function() {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('id', 'svg');
    svg.style.position = 'absolute';
    svg.style.top = 0;
    svg.style.left = 0;
    svg.style.width = '100%';
    svg.style.height = '100%';
    svg.style.pointerEvents = 'none';
    document.body.appendChild(svg);

    updatePositions();
};

window.addEventListener('resize', updatePositions);