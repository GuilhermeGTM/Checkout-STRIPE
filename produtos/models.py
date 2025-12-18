from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco =  models.FloatField(verbose_name='preço')
    

    def __str__(self):
        return self.nome
    
    #mostra o preço com 2 casas decimais formatado
    def exibe_preco(self):
        return "{:.2f}".format(self.preco)

class Pedido(models.Model):
    produto =  models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    payment_intent =  models.CharField(max_length=50, unique=True)
    email =  models.EmailField()
    valor_pago = models.IntegerField()
    status =  models.CharField(max_length=100)

    def __str__(self):
        return self.email
