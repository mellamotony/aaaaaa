from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Producto,Cliente,Pedido, DetallePedido,Usuario
from django.core.serializers import serialize



def home (request):
    return render ( request, 'home.html')

@csrf_exempt
def singup(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # Extraer los campos del JSON
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        password = data.get('password')

        # Crear una nueva instancia del modelo Producto
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
        )

        # Guardar el nuevo producto en la base de datos
        nuevo_usuario.save()

        return JsonResponse({'mensaje': 'Usuario creado correctamente'})

    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    
@csrf_exempt
def singout(request):
    logout(request)
    return JsonResponse({'mensaje': 'Cerrando cesion con exito'})

@csrf_exempt
def singin(request):
    if request.method == 'POST':
        # Verifica si el cuerpo de la solicitud contiene datos JSON
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)

        # Verifica si las claves 'username' y 'password' están presentes en los datos JSON
        if 'username' in data and 'password' in data:
            username = data['username']
            password = data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso'})
            else:
                return JsonResponse({'error': 'Usuario o contraseña incorrecta'}, status=401)
        else:
            return JsonResponse({'error': 'Datos de inicio de sesión incompletos'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt  # Usado para desactivar la protección CSRF,
def recibir_producto(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # Extraer los campos del JSON
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        stock = data.get('stock')
        imagen= data.get('imagen')

        # Crear una nueva instancia del modelo Producto
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            imagen= imagen
        )

        # Guardar el nuevo producto en la base de datos
        nuevo_producto.save()

        return JsonResponse({'mensaje': 'Producto creado correctamente'})

    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
   
@csrf_exempt  # Usado para desactivar la protección CSRF,
def actualizar_producto(request,id):
    if request.method== 'PATCH':
        try:
            # Obtener el producto existente
            producto = Producto.objects.get(pk=id)

            # Decodificar y obtener los datos del JSON
            data = json.loads(request.body.decode('utf-8'))

            # Actualizar los campos del producto con los nuevos datos
            producto.nombre = data.get('nombre', producto.nombre)
            producto.descripcion = data.get('descripcion', producto.descripcion)
            producto.precio = data.get('precio', producto.precio)
            producto.stock = data.get('stock', producto.stock)
            producto.imagen = data.get('imagen', producto.imagen)

            # Guardar los cambios en la base de datos
            producto.save()

            return JsonResponse({'mensaje': 'Producto actualizado con exito'})

        except Producto.DoesNotExist:
            return JsonResponse({'mensaje': 'Producto no encontrado'}, status=404)

    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def productos_view(request):
    productos = Producto.objects.all()
    # Serializar los productos a JSON
    productos_json = serialize('json', productos)
    # Devolver la respuesta como JSON
    return JsonResponse({'productos': productos_json}, safe=False)

@csrf_exempt  # Usado para desactivar la protección CSRF,
def cliente(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # Extraer los campos del JSON
        nombre = data.get('nombre')
        apellidop = data.get('apellidop')
        apellidom = data.get('apellidom')
        direccion = data.get('direccion')
        telefono= data.get('telefono')
        correo = data.get('correo')

        # Crear una nueva instancia del modelo Producto
        nuevo_cliente = Cliente(
            nombre=nombre,
            apellidop=apellidop,
            apellidom=apellidom,
            direccion=direccion,
            telefono= telefono,
            correo=correo
        )

        # Guardar el nuevo producto en la base de datos
        nuevo_cliente.save()
        
        return JsonResponse({'mensaje': 'Cliente creado con exito'})

    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@csrf_exempt  # Usado para desactivar la protección CSRF,
def actualizar_cliente(request,id):
    if request.method== 'PATCH':
        try:
            # Obtener el producto existente
            cliente = Cliente.objects.get(pk=id)

            # Decodificar y obtener los datos del JSON
            data = json.loads(request.body.decode('utf-8'))

            # Actualizar los campos del producto con los nuevos datos
            cliente.nombre = data.get('nombre', cliente.nombre)
            cliente.apellidop = data.get('apellidop', cliente.apellidop)
            cliente.apellidom = data.get('apellidom', cliente.apellidom)
            cliente.direccion = data.get('direccion', cliente.direccion)
            cliente.telefono = data.get('telefono', cliente.telefono)
            cliente.correo = data.get('correo', cliente.correo)

            # Guardar los cambios en la base de datos
            cliente.save()

            return JsonResponse({'mensaje': 'Cliente actualizado con exito'})

        except Cliente.DoesNotExist:
            return JsonResponse({'mensaje': 'Cliente no encontrado'}, status=404)

    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
   
def cliente_view(request):
    cliente = Cliente.objects.all()
    # Serializar los productos a JSON
    cliente_json = serialize('json', cliente)
    # Devolver la respuesta como JSON
    return JsonResponse({'cliente': cliente_json}, safe=False)

@csrf_exempt
def recibir_pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # Extraer los datos del pedido
        fecha_creacion = data.get('fecha_creacion')
        estado_pedido = data.get('estado_pedido')
        cliente_id = data.get('cliente_id')
        detalles_pedido = data.get('detalles_pedido', [])

        # Crear el objeto Pedido
        pedido = Pedido.objects.create(
            fecha_creacion=fecha_creacion,
            estado_pedido=estado_pedido,
            cliente_id=cliente_id
        )

        # Asociar detalles del pedido al pedido
        for detalle in detalles_pedido:
            producto_id = detalle.get('producto_id')
            cantidad = detalle.get('cantidad')

            try:
                producto = Producto.objects.get(id=producto_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad
                )
            except Producto.ObjectDoesNotExist:
                # Manejar el caso en que el producto no existe
                pass

        return JsonResponse({'mensaje': 'Pedido recibido correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def obtener_pedidos(request):
    pedidos = Pedido.objects.all()

    # Convierte los datos de los pedidos a un formato JSON
    pedidos_json = []
    for pedido in pedidos:
        detalles_pedido = DetallePedido.objects.filter(pedido=pedido)

        detalles_json = []
        for detalle in detalles_pedido:
            detalles_json.append({
                'producto_id': detalle.producto.id,
                'cantidad': detalle.cantidad,
                
            })

        pedidos_json.append({
            'id': pedido.id,
            'fecha_creacion': str(pedido.fecha_creacion),  # Convertir DateField a string para compatibilidad JSON
            'estado_pedido': pedido.estado_pedido,
            'cliente_id': pedido.cliente.id,
            'detalles_pedido': detalles_json
            
        })

    return JsonResponse({'pedidos': pedidos_json})




