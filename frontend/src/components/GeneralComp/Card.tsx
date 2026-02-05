import Image from 'next/image'
import Link from 'next/link'

interface CardProps {
  subTitle: string
  title: string
  para: string
  actionBtn: string
  link: string
  btnClass: string
  imgSource: string
}

const Card: React.FC<CardProps> = ({
  subTitle,
  title,
  para,
  actionBtn,
  link,
  btnClass,
  imgSource
}) => {
  return (
    <div className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
      <div className="relative h-48">
        <Image
          src={imgSource}
          alt={title}
          fill
          className="object-cover"
        />
      </div>

      <div className="p-6">
        <div className="text-sm font-semibold text-primary-600 uppercase tracking-wide mb-2">
          {subTitle}
        </div>

        <h3 className="text-xl font-bold text-gray-900 mb-3">
          {title}
        </h3>

        <p className="text-gray-600 mb-6 leading-relaxed">
          {para}
        </p>

        <Link
          href={link}
          className={`inline-block px-6 py-3 rounded-lg font-semibold transition-colors ${btnClass}`}
        >
          {actionBtn}
        </Link>
      </div>
    </div>
  )
}

export default Card