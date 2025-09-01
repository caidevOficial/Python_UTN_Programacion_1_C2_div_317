from utn_fra.funciones.image_reducer import ImageReducer


ir = ImageReducer('./test')
ir.reduce_image_weight()
ir.reduce_image_size(factor_escala=0.5)
ir.reduce_image_weight()