// $(document).ready(function () {
//   $('form').on('submit', function (event) {
//     $.ajax({
//       data: {
//         name: $('#nameInput').val(),
//         email: $('#emailInput').val()
//       },
//       type: 'POST',
//       url: '/process'
//     })
//       .done(function (data) {
//         if (data.error) {
//           $('#errorAlert').text(data.error).show()
//           $('#successAlert').hide()
//         } else {
//           $('#successAlert').text(data.name).show()
//           $('#errorAlert').hide()
//         }
//       })

//     event.preventDefault()
//   })
// })

<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
      <script type="application/javascript">
     $(document).ready(function(){
        $.getJSON("/",function(data){
            console.log(data.ext);
            var items =  [];
            $.each(data.ext, function(key, value){
            console.log(key);
            console.log(value);
            items.push('<li issuer=" ' + value.issuer + '">' + value.amount+    '</li>');
        });
        $('<ul/>', {
            'class': 'interest-list',
            html : items.join('')
        }).appendTo('body')
        });
    });
    </script> -->

     <!-- {% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}<br>
            {% for error in form.username.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
    <p>New User? <a href="{{ url_for('register') }}">Click to Register!</a></p>
{% endblock %} -->

