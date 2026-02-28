import sys
from copycat import main

if __name__ == '__main__':
    # Default to GUI mode unless --no-gui is specified
    if '--no-gui' in sys.argv:
        sys.argv.remove('--no-gui')
    elif '--gui' not in sys.argv and '--replay' not in sys.argv:
        sys.argv.append('--gui')
    main()
