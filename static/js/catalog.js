$('#btn-jordan').click(function() {
    $.ajax({
      url : 'catalog',
      type : 'GET',
      data : {
        brand : 'jordan',
      },
      success : function(response) {
        var message = response.message
      }
    });
  });