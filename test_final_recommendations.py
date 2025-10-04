#!/usr/bin/env python3
"""
Script de prueba final para verificar que el endpoint de recomendaciones funciona correctamente
"""

import asyncio
import sys
import os
sys.path.append('.')

from app.services.recommendations import get_game_recommendation

async def test_recommendations():
    """Probar todos los IDs que deberían funcionar"""
    
    print("🧪 PRUEBA FINAL DEL ENDPOINT DE RECOMENDACIONES")
    print("=" * 60)
    
    # IDs que deberían funcionar
    test_ids = [761140, 643980, 670290, 767400, 772540]
    
    success_count = 0
    
    for test_id in test_ids:
        print(f"\n🎯 Probando ID: {test_id}")
        print("-" * 30)
        
        try:
            result = await get_game_recommendation(test_id)
            
            if result and isinstance(result, list) and len(result) > 0:
                if 'error' in result[0]:
                    print(f"❌ Error: {result[0]['error']}")
                else:
                    print(f"✅ ÉXITO - {len(result)} recomendaciones encontradas:")
                    for i, game in enumerate(result, 1):
                        genres_str = ", ".join(game['genres'][:3]) + ("..." if len(game['genres']) > 3 else "")
                        dev_str = game['developer'][:25] + ("..." if len(game['developer']) > 25 else "")
                        print(f"   {i}. ID: {game['id']} | Dev: {dev_str} | Géneros: {genres_str}")
                    success_count += 1
            else:
                print(f"❌ Resultado vacío o inválido: {result}")
                
        except Exception as e:
            print(f"❌ Excepción: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN: {success_count}/{len(test_ids)} IDs funcionaron correctamente")
    
    if success_count == len(test_ids):
        print("🎉 ¡TODAS LAS PRUEBAS PASARON! El endpoint está funcionando correctamente.")
        return True
    else:
        print("⚠️  Algunas pruebas fallaron. Revisar los errores arriba.")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_recommendations())
    sys.exit(0 if result else 1)
